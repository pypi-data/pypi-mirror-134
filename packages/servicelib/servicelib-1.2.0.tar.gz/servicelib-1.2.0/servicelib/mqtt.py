# SPDX-FileCopyrightText: 2019-2021 Freemelt AB <opensource@freemelt.com>
#
# SPDX-License-Identifier: LGPL-3.0-only

"""MQTT related material"""

# Built-in
import logging
import json
import threading
import time
import re
import weakref

# Freemelt
import opcualib


class MQTTMessage:
    """Create MQTT message topic/payload that match MetricsRelay"""

    def __init__(self, topic, fields, tags=None, time_=None):
        self.topic = topic
        self.fields = fields
        self.tags = tags
        if time_ is None:
            time_ = time.time_ns()
        self.time = time_

    def _to_json(self, *args, **kwargs):
        p = self.fields.copy()
        p.update(time=str(self.time))
        if self.tags:
            p.update(_t=self.tags)
        return json.dumps(p, *args, **kwargs)

    @property
    def payload(self):
        return self._to_json()

    def __str__(self):
        p = self._to_json(indent=2)
        return f'{self.topic} = {p}'

    def __repr__(self):
        return f'{self.__class__.__name__}(topic={self.topic!r}, ' \
               f'fields={self.fields!r}, tags={self.tags!r}, ' \
               f'time_={self.time!r})'


class MQTTAttribute:

    instances = weakref.WeakSet()

    def __init__(self, topic, field, default='NA'):
        self.topic = topic
        self.field = field
        self.default = default
        # Convert topic wildcards to regexp
        _regex = re.sub(r'/\+/', '/[^/]+/', topic)
        self.topic_regex = re.compile(re.sub('#$', '.*', _regex) + '$')
        self.data = dict(time=-float('inf'))
        self.old_topic_alive = '/'.join(  # Backward compatibility
            topic.split('/')[:4] + ['Status', 'Alive'])
        self.topic_alive = '/'.join(
            topic.split('/')[:4] + ['ComponentStatus', 'Status', 'Current'])
        self.data_alive = dict(time=float('inf'))
        self.instances.add(self)

    @classmethod
    def topics(cls):
        output = set()
        for attr in cls.instances:
            output.add(attr.topic)
            output.add(attr.topic_alive)
            output.add(attr.old_topic_alive)
        return output

    def update(self, message):
        if message.topic in {self.topic_alive, self.old_topic_alive}:
            self.data_alive = json.loads(message.payload.decode('utf-8'))
        if self.topic_regex.match(message.topic):
            self.data = json.loads(message.payload.decode('utf-8'))

    def __get__(self, instance, owner=None):
        if not self.data_alive.get('alive'):
            # No alive-signal from the service
            return self.default
        if float(self.data_alive.get('time', 'inf')) >= \
                float(self.data.get('time', '-inf')):
            # Data older that alive-signal
            return self.default
        # Return field data if it exists
        return self.data.get(self.field, self.default)

    def __set__(self, instance, value):
        raise AttributeError("Can't set attribute")


class BaseMetricsPublisherThread(threading.Thread):
    """Continuously publish metrics to mqtt broker.

    This class should be subclassed and implement the `get_messages`
    method.
    """

    def __init__(self, mqtt_client, interval=1, **kwargs):
        super().__init__(**kwargs)
        self.stop_event = threading.Event()
        self.mqtt = mqtt_client
        self.interval = interval
        self.log = logging.getLogger('MetricsPublisher')

    def stop(self):
        self.stop_event.set()

    def run(self):
        """Metrics Publisher thread entry point

        Continuously publish metrics to mqtt broker.
        """
        self.log.info("Metrics Publisher thread started")
        messages = list()
        responses = list()

        while not self.stop_event.is_set():
            for resp in responses:
                if not resp.is_published():
                    self.log.warning('MQTT message not yet published.')
            responses.clear()

            self.log.debug('About to read all OPC sensor values ...')
            messages.clear()
            try:
                # Read OPC variables
                messages += self.get_messages()
            except opcualib.PLCTimeoutError:
                self.stop()
            except Exception:
                self.log.exception("MetricsPublisher failed")

            self.log.debug(
                'Publishing %d messages of OPC sensor values to MQTT broker.',
                len(messages))

            for m in messages:
                try:
                    resp = self.mqtt.publish(m.topic, m.payload, retain=True)
                except Exception:
                    self.log.exception('Failed when publishing %s', m)
                else:
                    responses.append(resp)

            self.log.debug(
                'Sleeping for %.1f sec before reading sensor values again.',
                self.interval)
            # Read new value every second
            self.stop_event.wait(self.interval)

        self.log.info("Metrics Publisher thread loop completed")

    def get_messages(self):
        """Return list of `MQTTMessage` instances"""
        raise NotImplementedError
