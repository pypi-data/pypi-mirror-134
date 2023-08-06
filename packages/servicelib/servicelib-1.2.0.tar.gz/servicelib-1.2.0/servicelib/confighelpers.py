# SPDX-FileCopyrightText: 2019-2021 Freemelt AB <opensource@freemelt.com>
#
# SPDX-License-Identifier: LGPL-3.0-only

"""Types and functions shared between services"""

# Built-in
import logging
import contextlib
import concurrent.futures
import inspect
import sys
import time

# PyPI
import grpc
import paho.mqtt.client as mqtt
import systemd.journal

# Freemelt
import opcualib

# Project
from .mqtt import MQTTMessage


def setup_logging(cfg, journal_kwargs):
    # Set log levels.
    if sys.stdout.isatty():
        console_fmt = (
            '%(relativeCreated)d:%(levelname)s:%(threadName)s:%(name)s: '
            '%(message)s')
        handler = logging.StreamHandler(sys.stdout)
    else:
        console_fmt = '%(levelname)s:%(threadName)s:%(name)s: %(message)s'
        handler = systemd.journal.JournalHandler(**journal_kwargs)
    for name, value in cfg["Service:Loglevels"].block.items():
        if name == 'root':
            name = ''
        logging.getLogger(name).setLevel(value)
    console_formatter = logging.Formatter(fmt=console_fmt)
    handler.setFormatter(console_formatter)
    root = logging.getLogger()
    root.addHandler(handler)


def get_opc_client(cfg):
    host = cfg.get_str("Service:OPC:IP")
    port = cfg.get_int("Service:OPC:Port")
    base_path = cfg.get_str("OPC:Base")
    namespace = cfg.get_str("OPC:Namespace")
    # import unittest.mock
    # return unittest.mock.MagicMock()
    client = opcualib.SyncClient(host, port, namespace, base_path)
    client.path_transform = lambda path: cfg.get_str(f'OPC:{path}')
    return client


@contextlib.contextmanager
def get_mqtt_client(cfg, *userdata, client_id=''):
    """Create mqtt client for service"""
    log = logging.getLogger('MQTT')
    log.info('Connecting to MQTT broker ...')
    mqtt_client = mqtt.Client(
        client_id=client_id,
        clean_session=True,
        userdata=(cfg, *userdata))
    topic_base = cfg['Service:MQTT:TopicBase']

    # This is the old alive/dead convention
    # These are still used for backward compatibility
    old_msg_dead = MQTTMessage(f'{topic_base}/Status/Alive', dict(alive=False))
    old_msg_alive = MQTTMessage(f'{topic_base}/Status/Alive', dict(alive=True))

    # This is the new alive/dead convention
    msg_dead = MQTTMessage(
        f'{topic_base}/ComponentStatus/Status/Current', dict(alive=False))
    msg_alive = MQTTMessage(
        f'{topic_base}/ComponentStatus/Status/Current', dict(alive=True))

    mqtt_client.enable_logger(log)
    mqtt_client.will_set(msg_dead.topic, msg_dead.payload, retain=True)
    mqtt_client.will_set(old_msg_dead.topic, old_msg_dead.payload, retain=True)
    mqtt_client.connect(
        host=cfg['Service:MQTT:IP'],
        port=cfg['Service:MQTT:Port']
    )
    mqtt_client.loop_start()
    resp = mqtt_client.publish(msg_alive.topic, msg_alive.payload, retain=True)
    mqtt_client.publish(old_msg_alive.topic, old_msg_alive.payload, retain=True)
    log.info('Publish status alive = True ...')
    for _ in range(30):
        if resp.is_published():
            break
        time.sleep(0.5)
    else:
        log.warning('Failed to publish status alive = True.')
    log.info('Connected to MQTT broker and published status alive.')
    try:
        yield mqtt_client
        log.info('Publish status alive = False ...')
        resp = mqtt_client.publish(
            msg_dead.topic, msg_dead.payload, retain=True)
        mqtt_client.publish(
            old_msg_dead.topic, old_msg_dead.payload, retain=True)
        for _ in range(10):
            if resp.is_published():
                break
            time.sleep(0.5)
        else:
            log.warning('Failed to publish status alive = False.')
        log.info('Disconnecting ...')
        mqtt_client.disconnect()
        log.info('Disconnected.')
    finally:
        log.info('Stopping MQTT loop ...')
        mqtt_client.loop_stop()
        log.info('MQTT loop stopped.')


@contextlib.contextmanager
def get_grpc_server(cfg, rpc, servicer):
    executor = concurrent.futures.ThreadPoolExecutor(
        thread_name_prefix='gRPC-worker')
    server = grpc.server(executor)
    members = inspect.getmembers(rpc)
    add_to_server = [f for n, f in members if
                     n.startswith('add') and n.endswith('_to_server')]
    assert add_to_server
    add_to_server[0](servicer, server)
    rpc_host = cfg.get_str("Service:GRPC:IP")
    rpc_port = cfg.get_int("Service:GRPC:Port")
    server.add_insecure_port(f"{rpc_host}:{rpc_port}")
    server.start()
    log = logging.getLogger('gRPC-server')
    try:
        yield server
    finally:
        log.info('Stopping gRPC server ...')
        server.stop(grace=3)
        log.info('gRPC server stopped.')
