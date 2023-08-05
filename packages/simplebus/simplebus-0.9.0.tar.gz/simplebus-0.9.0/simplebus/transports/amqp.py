# Copyright 2015 Vinicius Chiele. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""AMQP transport implementation."""


try:
    import amqpstorm
except ImportError:
    amqpstorm = None

import logging
import uuid

from simplebus.pools import ResourcePool
from simplebus.transports import base
from simplebus.utils import EventHandler
from threading import Lock
from threading import Thread
from urllib import parse

LOGGER = logging.getLogger(__name__)


class Transport(base.Transport):
    def __init__(self, url):
        if amqpstorm is None:
            raise ImportError('Missing amqp-storm library (pip install amqp-storm)')

        self.__connection = None
        self.__connection_lock = Lock()
        self.__channels = None
        self.__channel_limit = self.__parse_channel_limit(url)
        self.__close_lock = Lock()
        self.__closed_by_user = None
        self.__url = url
        self.__pullers = {}
        self.__subscribers = {}
        self.closed = EventHandler()

    @property
    def is_open(self):
        return self.__connection and self.__connection.is_open

    def open(self):
        if self.is_open:
            return
        self.__ensure_connection()

    def close(self):
        if not self.is_open:
            return
        self.__close(True)

    def cancel(self, id):
        puller = self.__pullers.pop(id, None)
        if puller:
            puller.error -= self.__on_consumer_error
            puller.stop()

    def push(self, queue, message, options):
        self.__ensure_connection()
        self.__send_message('', queue, message, True)

    def pull(self, id, queue, callback, options):
        self.__ensure_connection()

        puller = Puller(self.__connection, queue, callback, options)
        puller.error += self.__on_consumer_error
        puller.start()
        self.__pullers[id] = puller

    def publish(self, topic, message, options):
        self.__ensure_connection()
        self.__send_message(topic, '', message, False)

    def subscribe(self, id, topic, callback, options):
        self.__ensure_connection()

        subscriber = Subscriber(self.__connection, topic, callback, options)
        subscriber.error += self.__on_consumer_error
        subscriber.start()
        self.__subscribers[id] = subscriber

    def unsubscribe(self, id):
        subscriber = self.__subscribers.pop(id, None)
        if subscriber:
            subscriber.error -= self.__on_consumer_error
            subscriber.stop()

    def __close(self, by_user):
        self.__closed_by_user = by_user

        for id in dict.fromkeys(self.__pullers):
            self.cancel(id)

        for id in dict.fromkeys(self.__subscribers):
            self.unsubscribe(id)

        if self.__channels:
            self.__channels.close()
            self.__channels = None

        if self.__connection:
            self.__connection.close()
            self.__connection = None

        if self.closed:
            self.closed(by_user)

    def __ensure_connection(self):
        if self.is_open:
            return

        if not self.__connection_lock.acquire(timeout=0.1):
            raise ConnectionError('Transport is closed.')

        try:
            if self.is_open:
                return

            self.__connection = amqpstorm.UriConnection(self.__url)
            self.__connection.open()
            self.__closed_by_user = None
            self.__channels = ChannelPool(self.__channel_limit, self.__connection)
        finally:
            self.__connection_lock.release()

    def __on_consumer_error(self, consumer, e):
        # if the transport was closed by the user this error should have occurred
        # because the connection was closed, so ignore it.
        if self.__closed_by_user:
            return

        if self.__close_lock.acquire(False):
            try:
                if self.__closed_by_user is not None:
                    return
                # whatever the error closes the connection.
                LOGGER.critical('Connection to the broker went down.', exc_info=True)

                self.__close(False)
            finally:
                self.__close_lock.release()

    @staticmethod
    def __parse_channel_limit(url):
        uri = parse.urlparse(url)
        params = parse.parse_qs(uri.query)

        channel_limit = params.get('channel_limit')

        if not channel_limit:
            return None

        return int(channel_limit[0])

    def __send_message(self, exchange, routing_key, message, mandatory):
        properties = {
            'app_id': message.app_id,
            'message_id': message.message_id,
            'content_type': message.content_type,
            'content_encoding': message.content_encoding,
            'delivery_mode': 2
        }

        if message.expiration:
            properties['expiration'] = str(message.expiration)

        if message.retry_count > 0:
            properties['headers'] = {'x-retry-count': message.retry_count}

        channel = self.__channels.acquire()
        try:
            channel.confirm_deliveries()
            channel.basic.publish(message.body, routing_key, exchange, mandatory=mandatory, properties=properties)
        finally:
            self.__channels.release(channel)


class TransportMessage(base.TransportMessage):
    def __init__(self, body, method, properties, channel, dead_letter_queue=None, retry_queue=None):
        super().__init__(body=body)

        self.__method = method
        self.__properties = properties
        self.__channel = channel
        self.__dead_letter_queue = dead_letter_queue
        self.__retry_queue = retry_queue

        app_id = properties.get('app_id')
        if app_id:
            self.app_id = bytes.decode(app_id)

        message_id = properties.get('message_id')
        if message_id:
            self.message_id = bytes.decode(message_id)

        content_type = properties.get('content_type')
        if content_type:
            self.content_type = bytes.decode(content_type)

        content_encoding = properties.get('content_encoding')
        if content_encoding:
            self.content_encoding = bytes.decode(content_encoding)

        headers = properties.get('headers')
        if not headers:
            headers = {}
            properties['headers'] = headers

        self._retry_count = headers.get(bytes('x-retry-count', 'utf-8')) or 0

        expiration = self.__properties.get('expiration')
        if expiration:
            self.expiration = int(expiration)

    def delete(self):
        if self.__channel:
            self.__channel.basic.ack(self.__method.get('delivery_tag'))
            self.__channel = None

    def dead_letter(self, reason):
        if self.__channel:
            self.__set_header_retry_count(0)
            self.__set_header_death_reason(reason)

            self.__channel.basic.ack(self.__method.get('delivery_tag'))

            if not self.__dead_letter_queue:
                return

            self.__channel.basic.publish(
                self.body,
                self.__dead_letter_queue,
                '',
                self.__properties)
            self.__channel = None

    def retry(self):
        if self.__channel:
            self.__set_header_retry_count(self.retry_count + 1)

            if self.__retry_queue:
                routing_key = self.__retry_queue
                exchange = ''
            else:
                routing_key = str(self.__method.get('routing_key'), encoding='utf-8')
                exchange = str(self.__method.get('exchange'), encoding='utf-8')

            self.__channel.basic.ack(self.__method.get('delivery_tag'))
            self.__channel.basic.publish(
                self.body,
                routing_key,
                exchange,
                self.__properties)

    def __set_header_death_reason(self, reason):
        headers = self.__properties.get('headers')
        headers[bytes('x-death-reason', 'utf-8')] = reason

    def __set_header_retry_count(self, retry_count):
        headers = self.__properties.get('headers')
        headers[bytes('x-retry-count', 'utf-8')] = retry_count


class ChannelPool(ResourcePool):
    """Provides a pool of channels."""

    def __init__(self, max_size, connection):
        super().__init__(max_size)
        self.__connection = connection

    def _create_resource(self):
        """Creates a new channel."""
        return self.__connection.channel()

    def _close_resource(self, resource):
        """Close the specified channel."""
        resource.close()

    def _validate_resource(self, resource):
        """Validates whether channel is open."""
        return resource.is_open


class Consumer(object):
    def __init__(self, connection):
        self.__connection = connection
        self.error = EventHandler()

    def _create_dead_letter_queue(self, dead_letter_queue):
        with self.__connection.channel() as channel:
            channel.queue.declare(dead_letter_queue, durable=True)

    def _create_retry_queue(self, queue, retry_queue, retry_delay):
        args = {
            'x-dead-letter-exchange': '',
            'x-dead-letter-routing-key': queue,
            'x-message-ttl': retry_delay}

        try:
            with self.__connection.channel() as channel:
                channel.queue.declare(retry_queue, durable=True, arguments=args)
        except amqpstorm.AMQPChannelError as e:
            if 'x-message-ttl' not in str(e):  # already exists a queue with ttl
                raise

    def _start_receiving(self, channel):
        try:
            channel.start_consuming()
        except Exception as e:
            self.error(self, e)


class Puller(Consumer):
    def __init__(self, connection, queue, callback, options):
        super().__init__(connection)

        self.__connection = connection
        self.__queue = queue
        self.__callback = callback
        self.__channels = []

        self.__dead_letter = options.get('dead_letter')
        self.__retry = options.get('retry')
        self.__max_retries = options.get('max_retries')
        self.__retry_delay = options.get('retry_delay')
        self.__max_concurrency = options.get('max_concurrency')
        self.__prefetch_count = options.get('prefetch_count')

        self.__dead_letter_queue = None
        self.__retry_queue = None

        if self.__dead_letter:
            self.__dead_letter_queue = queue + '.error'

        if self.__retry:
            self.__retry_queue = queue
            if self.__retry_delay > 0:
                self.__retry_queue += '.retry'

    def start(self):
        if self.__dead_letter:
            self._create_dead_letter_queue(self.__dead_letter_queue)

        if self.__retry and self.__retry_delay > 0:
            self._create_retry_queue(self.__queue, self.__retry_queue, self.__retry_delay)

        for i in range(self.__max_concurrency):
            channel = self.__connection.channel()
            channel.queue.declare(self.__queue, durable=True)
            channel.basic.qos(self.__prefetch_count)
            channel.basic.consume(self.__on_message, self.__queue)
            self.__channels.append(channel)

            thread = Thread(target=self._start_receiving, args=(channel,))
            thread.daemon = True
            thread.start()

    def stop(self):
        for channel in self.__channels:
            channel.close()

        self.__channels.clear()

    def __on_message(self, body, channel, method, properties):
        try:
            message = TransportMessage(body, method, properties, channel,
                                       self.__dead_letter_queue, self.__retry_queue)

            if self.__retry and message.retry_count > self.__max_retries:
                message.dead_letter('Max retries exceeded.')
            else:
                self.__callback(message)
        except:
            LOGGER.exception("Puller failed, queue '%s'." % self.__queue)


class Subscriber(Consumer):
    def __init__(self, connection, topic, callback, options):
        super().__init__(connection)

        self.__connection = connection
        self.__topic = topic
        self.__callback = callback
        self.__channels = []

        self.__queue = topic + ':' + str(uuid.uuid4()).replace('-', '')
        self.__max_concurrency = options.get('max_concurrency')
        self.__prefetch_count = options.get('prefetch_count')

    def start(self):
        for i in range(self.__max_concurrency):
            channel = self.__connection.channel()
            channel.exchange.declare(self.__topic, 'topic', durable=True)
            channel.queue.declare(self.__queue, auto_delete=True)
            channel.queue.bind(self.__queue, self.__topic)
            channel.basic.consume(self.__on_message, self.__queue)
            self.__channels.append(channel)

            thread = Thread(target=self._start_receiving, args=(channel,))
            thread.daemon = True
            thread.start()

    def stop(self):
        for channel in self.__channels:
            channel.close()

        self.__channels.clear()

    def __on_message(self, body, channel, method, properties):
        try:
            message = TransportMessage(body, method, properties, channel)
            self.__callback(message)
        except:
            LOGGER.exception("Subscriber failed, topic: '%s'." % self.__topic)
