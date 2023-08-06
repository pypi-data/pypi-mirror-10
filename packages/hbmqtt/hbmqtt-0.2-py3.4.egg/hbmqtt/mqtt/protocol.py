# Copyright (c) 2015 Nicolas JOUANIN
#
# See the file license.txt for copying permission.
import logging
import asyncio
from asyncio import futures
from hbmqtt.mqtt.packet import MQTTFixedHeader
from hbmqtt.mqtt import packet_class
from hbmqtt.errors import NoDataException
from hbmqtt.mqtt.packet import PacketType
from hbmqtt.mqtt.connect import ConnectVariableHeader, ConnectPacket, ConnectPayload
from hbmqtt.mqtt.connack import ConnackPacket
from hbmqtt.mqtt.disconnect import DisconnectPacket
from hbmqtt.mqtt.pingreq import PingReqPacket
from hbmqtt.mqtt.pingresp import PingRespPacket
from hbmqtt.mqtt.publish import PublishPacket
from hbmqtt.mqtt.pubrel import PubrelPacket
from hbmqtt.mqtt.puback import PubackPacket
from hbmqtt.mqtt.pubrec import PubrecPacket
from hbmqtt.mqtt.pubcomp import PubcompPacket
from hbmqtt.mqtt.subscribe import SubscribePacket
from hbmqtt.mqtt.suback import SubackPacket
from hbmqtt.mqtt.unsubscribe import UnsubscribePacket
from hbmqtt.mqtt.unsuback import UnsubackPacket
from hbmqtt.session import Session
from transitions import Machine, MachineError

class InFlightMessage:
    states = ['new', 'published', 'acknowledged', 'received', 'released', 'completed']

    def __init__(self, packet, qos):
        self.packet = packet
        self.qos = qos
        self.puback = None
        self.pubrec = None
        self.pubcomp = None
        self.pubrel = None
        self._init_states()

    def _init_states(self):
        self.machine = Machine(model=self, states=InFlightMessage.states, initial='new')
        self.machine.add_transition(trigger='publish', source='new', dest='published')
        if self.qos == 0x01:
            self.machine.add_transition(trigger='acknowledge', source='published', dest='acknowledged')
        if self.qos == 0x02:
            self.machine.add_transition(trigger='receive', source='published', dest='received')
            self.machine.add_transition(trigger='release', source='received', dest='released')
            self.machine.add_transition(trigger='complete', source='released', dest='completed')


class ProtocolHandler:
    """
    Class implementing the MQTT communication protocol using asyncio features
    """

    def __init__(self, session: Session, config, loop=None):
        self.logger = logging.getLogger(__name__)
        self.session = session
        self.config = config
        if loop is None:
            self._loop = asyncio.get_event_loop()
        else:
            self._loop = loop
        self._reader_task = None
        self._writer_task = None
        self._reader_ready = asyncio.Event(loop=self._loop)
        self._writer_ready = asyncio.Event(loop=self._loop)

        self._running = False

        self.session.local_address, self.session.local_port = self.session.writer.get_extra_info('sockname')

        self.incoming_queues = dict()
        self.application_messages = asyncio.Queue()
        for p in PacketType:
            self.incoming_queues[p] = asyncio.Queue()
        self.outgoing_queue = asyncio.Queue()
        self._puback_waiters = dict()
        self._pubrec_waiters = dict()
        self._pubrel_waiters = dict()
        self._pubcomp_waiters = dict()
        self.delivered_message = asyncio.Queue()

    @asyncio.coroutine
    def start(self):
        self._running = True
        self._reader_task = asyncio.async(self._reader_coro(), loop=self._loop)
        self._writer_task = asyncio.async(self._writer_coro(), loop=self._loop)
        yield from asyncio.wait(
            [self._reader_ready.wait(), self._writer_ready.wait()], loop=self._loop)
        self.logger.debug("Handler tasks started")

    @asyncio.coroutine
    def mqtt_publish(self, topic, message, packet_id, dup, qos, retain):
        if packet_id in self.session.inflight_out:
            self.logger.warn("A message with the same packet ID is already in flight")
        packet = PublishPacket.build(topic, message, packet_id, dup, qos, retain)
        yield from self.outgoing_queue.put(packet)
        inflight_message = InFlightMessage(packet, qos)
        self.session.inflight_out[packet.variable_header.packet_id] = inflight_message

        inflight_message.publish()
        if qos == 0x01:
            waiter = futures.Future(loop=self._loop)
            self._puback_waiters[packet_id] = waiter
            yield from waiter
            inflight_message.puback = waiter.result()
            inflight_message.acknowledge()
            del self._puback_waiters[packet_id]
        if qos == 0x02:
            # Wait for PUBREC
            waiter = futures.Future(loop=self._loop)
            self._pubrec_waiters[packet_id] = waiter
            yield from waiter
            inflight_message.pubrec = waiter.result()
            del self._pubrec_waiters[packet_id]
            inflight_message.receive()

            # Send pubrel
            pubrel = PubrelPacket.build(packet_id)
            yield from self.outgoing_queue.put(pubrel)
            inflight_message.pubrel = pubrel
            inflight_message.release()

            # Wait for pubcomp
            waiter = futures.Future(loop=self._loop)
            self._pubcomp_waiters[packet_id] = waiter
            yield from waiter
            inflight_message.pubcomp = waiter.result()
            del self._pubcomp_waiters[packet_id]
            inflight_message.complete()

        del self.session.inflight_out[packet_id]
        return inflight_message

    @asyncio.coroutine
    def stop(self):
        self._running = False
        self.session.reader.feed_eof()
        yield from asyncio.wait([self._writer_task, self._reader_task], loop=self._loop)

    @asyncio.coroutine
    def _reader_coro(self):
        self.logger.debug("Starting reader coro")
        while self._running:
            try:
                self._reader_ready.set()
                fixed_header = yield from asyncio.wait_for(MQTTFixedHeader.from_stream(self.session.reader), 5)
                if fixed_header:
                    cls = packet_class(fixed_header)
                    packet = yield from cls.from_stream(self.session.reader, fixed_header=fixed_header)
                    self.logger.debug(" <-in-- " + repr(packet))

                    if packet.fixed_header.packet_type == PacketType.CONNACK:
                        asyncio.Task(self.handle_connack(packet))
                    elif packet.fixed_header.packet_type == PacketType.SUBACK:
                        asyncio.Task(self.handle_suback(packet))
                    elif packet.fixed_header.packet_type == PacketType.UNSUBACK:
                        asyncio.Task(self.handle_unsuback(packet))
                    elif packet.fixed_header.packet_type == PacketType.PUBACK:
                        asyncio.Task(self.handle_puback(packet))
                    elif packet.fixed_header.packet_type == PacketType.PUBREC:
                        asyncio.Task(self.handle_pubrec(packet))
                    elif packet.fixed_header.packet_type == PacketType.PUBREL:
                        asyncio.Task(self.handle_pubrel(packet))
                    elif packet.fixed_header.packet_type == PacketType.PUBCOMP:
                        asyncio.Task(self.handle_pubcomp(packet))
                    elif packet.fixed_header.packet_type == PacketType.PINGRESP:
                        asyncio.Task(self.handle_pingresp(packet))
                    elif packet.fixed_header.packet_type == PacketType.PUBLISH:
                        asyncio.Task(self.handle_publish(packet))
                    else:
                        self.logger.warn("Unhandled packet type: %s" % packet.fixed_header.packet_type)
                else:
                    self.logger.debug("No more data, stopping reader coro")
                    break
            except asyncio.TimeoutError:
                self.logger.debug("Input stream read timeout")
            except NoDataException as nde:
                self.logger.debug("No data available")
            except Exception as e:
                self.logger.warn("Unhandled exception in reader coro: %s" % e)
                break
        self.logger.debug("Reader coro stopped")

    @asyncio.coroutine
    def _writer_coro(self):
        self.logger.debug("Starting writer coro")
        keepalive_timeout = self.session.keep_alive - self.config['ping_delay']
        while self._running:
            try:
                self._writer_ready.set()
                packet = yield from asyncio.wait_for(self.outgoing_queue.get(), keepalive_timeout)
                yield from packet.to_stream(self.session.writer)
                self.logger.debug(" -out-> " + repr(packet))
                yield from self.session.writer.drain()
                #self.outgoing_queue.task_done() # to be used with Python 3.5
            except asyncio.TimeoutError as ce:
                self.logger.debug("Output queue get timeout")
                if self._running:
                    self.logger.debug("PING for keepalive")
                    self.handle_keepalive()
            except Exception as e:
                self.logger.warn("Unhandled exception in writer coro: %s" % e)
                break
        self.logger.debug("Writer coro stopping")
        # Flush queue before stopping
        if not self.outgoing_queue.empty():
            while True:
                try:
                    packet = self.outgoing_queue.get_nowait()
                    yield from packet.to_stream(self.session.writer)
                    self.logger.debug(" -out-> " + repr(packet))
                except asyncio.QueueEmpty:
                    break
                except Exception as e:
                    self.logger.warn("Unhandled exception in writer coro: %s" % e)
        self.logger.debug("Writer coro stopped")

    @asyncio.coroutine
    def mqtt_deliver_next_message(self):
        inflight_message = yield from self.delivered_message.get()
        return inflight_message

    def handle_keepalive(self):
        pass

    @asyncio.coroutine
    def handle_connack(self, connack: ConnackPacket):
        pass

    @asyncio.coroutine
    def handle_suback(self, suback: SubackPacket):
        pass

    @asyncio.coroutine
    def handle_unsuback(self, unsuback: UnsubackPacket):
        pass

    @asyncio.coroutine
    def handle_pingresp(self, pingresp: PingRespPacket):
        pass

    @asyncio.coroutine
    def handle_puback(self, puback: PubackPacket):
        packet_id = puback.variable_header.packet_id
        try:
            waiter = self._puback_waiters[packet_id]
            waiter.set_result(puback)
        except KeyError as ke:
            self.logger.warn("Received PUBACK for unknown pending subscription with Id: %s" % packet_id)

    @asyncio.coroutine
    def handle_pubrec(self, pubrec: PubrecPacket):
        packet_id = pubrec.variable_header.packet_id
        try:
            waiter = self._pubrec_waiters[packet_id]
            waiter.set_result(pubrec)
        except KeyError as ke:
            self.logger.warn("Received PUBREC for unknown pending subscription with Id: %s" % packet_id)

    @asyncio.coroutine
    def handle_pubcomp(self, pubcomp: PubcompPacket):
        packet_id = pubcomp.variable_header.packet_id
        try:
            waiter = self._pubcomp_waiters[packet_id]
            waiter.set_result(pubcomp)
        except KeyError as ke:
            self.logger.warn("Received PUBCOMP for unknown pending subscription with Id: %s" % packet_id)

    @asyncio.coroutine
    def handle_pubrel(self, pubrel: PubrecPacket):
        packet_id = pubrel.variable_header.packet_id
        try:
            waiter = self._pubrel_waiters[packet_id]
            waiter.set_result(pubrel)
        except KeyError as ke:
            self.logger.warn("Received PUBREL for unknown pending subscription with Id: %s" % packet_id)

    @asyncio.coroutine
    def handle_publish(self, publish : PublishPacket):
        inflight_message = None
        packet_id = publish.variable_header.packet_id
        qos = (publish.fixed_header.flags >> 1) & 0x03
        if packet_id in self.session.inflight_in:
            inflight_message = self.session.inflight_in[packet_id]
        else:
            inflight_message = InFlightMessage(publish, qos)
            self.session.inflight_in[packet_id] = inflight_message
            inflight_message.publish()

        if qos == 1:
            puback = PubackPacket.build(packet_id)
            yield from self.outgoing_queue.put(puback)
            inflight_message.acknowledge()
        if qos == 2:
            pubrec = PubrecPacket.build(packet_id)
            yield from self.outgoing_queue.put(pubrec)
            inflight_message.receive()
            waiter = futures.Future(loop=self._loop)
            self._pubrel_waiters[packet_id] = waiter
            yield from waiter
            inflight_message.pubrel = waiter.result()
            del self._pubrel_waiters[packet_id]
            inflight_message.release()
            pubcomp = PubcompPacket.build(packet_id)
            yield from self.outgoing_queue.put(pubcomp)
            inflight_message.complete()
        yield from self.delivered_message.put(inflight_message)
        del self.session.inflight_in[packet_id]

class ClientProtocolHandler(ProtocolHandler):
    def __init__(self, session: Session, config, loop=None):
        super().__init__(session, config, loop)
        self._ping_task = None
        self._connack_waiter = None
        self._pingresp_queue = asyncio.Queue()
        self._subscriptions_waiter = dict()
        self._unsubscriptions_waiter = dict()

    @asyncio.coroutine
    def start(self):
        yield from super().start()

    @asyncio.coroutine
    def stop(self):
        yield from super().stop()
        if self._ping_task:
            try:
                self._ping_task.cancel()
            except Exception:
                pass

    def handle_keepalive(self):
        self._ping_task = self._loop.call_soon(asyncio.async, self.mqtt_ping())

    @asyncio.coroutine
    def mqtt_subscribe(self, topics, packet_id):
        """
        :param topics: array of topics [{'filter':'/a/b', 'qos': 0x00}, ...]
        :return:
        """
        subscribe = SubscribePacket.build(topics, packet_id)
        yield from self.outgoing_queue.put(subscribe)
        waiter = futures.Future(loop=self._loop)
        self._subscriptions_waiter[subscribe.variable_header.packet_id] = waiter
        return_codes = yield from waiter
        del self._subscriptions_waiter[subscribe.variable_header.packet_id]
        return return_codes

    @asyncio.coroutine
    def handle_suback(self, suback: SubackPacket):
        packet_id = suback.variable_header.packet_id
        try:
            waiter = self._subscriptions_waiter.get(packet_id)
            waiter.set_result(suback.payload.return_codes)
        except KeyError as ke:
            self.logger.warn("Received SUBACK for unknown pending subscription with Id: %s" % packet_id)

    @asyncio.coroutine
    def mqtt_unsubscribe(self, topics, packet_id):
        """

        :param topics: array of topics ['/a/b', ...]
        :return:
        """
        unsubscribe = UnsubscribePacket.build(topics, packet_id)
        yield from self.outgoing_queue.put(unsubscribe)
        waiter = futures.Future(loop=self._loop)
        self._unsubscriptions_waiter[unsubscribe.variable_header.packet_id] = waiter
        yield from waiter
        del self._unsubscriptions_waiter[unsubscribe.variable_header.packet_id]

    @asyncio.coroutine
    def handle_unsuback(self, unsuback: UnsubackPacket):
        packet_id = unsuback.variable_header.packet_id
        try:
            waiter = self._unsubscriptions_waiter.get(packet_id)
            waiter.set_result(None)
        except KeyError as ke:
            self.logger.warn("Received UNSUBACK for unknown pending subscription with Id: %s" % packet_id)

    @asyncio.coroutine
    def mqtt_connect(self):
        def build_connect_packet(session):
            vh = ConnectVariableHeader()
            payload = ConnectPayload()

            vh.keep_alive = session.keep_alive
            vh.clean_session_flag = session.clean_session
            vh.will_retain_flag = session.will_retain
            payload.client_id = session.client_id

            if session.username:
                vh.username_flag = True
                payload.username = session.username
            else:
                vh.username_flag = False

            if session.password:
                vh.password_flag = True
                payload.password = session.password
            else:
                vh.password_flag = False
            if session.will_flag:
                vh.will_flag = True
                vh.will_qos = session.will_qos
                payload.will_message = session.will_message
                payload.will_topic = session.will_topic
            else:
                vh.will_flag = False

            header = MQTTFixedHeader(PacketType.CONNECT, 0x00)
            packet = ConnectPacket(header, vh, payload)
            return packet

        packet = build_connect_packet(self.session)
        yield from self.outgoing_queue.put(packet)
        self._connack_waiter = futures.Future(loop=self._loop)
        return (yield from self._connack_waiter)

    @asyncio.coroutine
    def handle_connack(self, connack: ConnackPacket):
        self._connack_waiter.set_result(connack.variable_header.return_code)

    @asyncio.coroutine
    def mqtt_disconnect(self):
        # yield from self.outgoing_queue.join() To be used in Python 3.5
        disconnect_packet = DisconnectPacket()
        yield from self.outgoing_queue.put(disconnect_packet)
        self._connack_waiter = None

    @asyncio.coroutine
    def mqtt_ping(self):
        ping_packet = PingReqPacket()
        yield from self.outgoing_queue.put(ping_packet)
        self._pingresp_waiter = futures.Future(loop=self._loop)
        resp = yield from self._pingresp_queue.get()
        return resp

    @asyncio.coroutine
    def handle_pingresp(self, pingresp: PingRespPacket):
        yield from self._pingresp_queue.put(pingresp)
