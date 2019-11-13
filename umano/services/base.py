from abc import ABC
from datetime import datetime, timedelta
from enum import IntEnum, auto
from optparse import make_option, OptionParser
import socket
import sys
import time
from uuid import uuid4

from kombu import Consumer

from hal.messages import get_connection, get_queue_for_dataclass
from umano.hal.data import store, find, updated_after

import logging


class STATUS(IntEnum):
    IDLE = auto()
    COMPUTING = auto()
    PLAYING = auto()
    ERROR = auto()
    TOUCHING = auto()
    ACQUIRING = auto()
    STREAMING = auto()
    TERMINATED = auto()


class UmanoService(object):
    help = "unknown umano service usage"
    option_list = [
        make_option(
            '--name',
            dest='NAME',
            type=str,
            default="",
            help='service name (default "unknown-<uuid>")'
        ),
        make_option(
            '--description',
            dest='DESCRIPTION',
            type=str,
            default="",
            help='service description (default "")'
        ),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.name = "unknown-{}".format(str(uuid4())[:8])
        self.description = "no description"
        self.status = None
        self.status_document = None
        self.host = socket.gethostname()
        self.ip = socket.gethostbyname(self.host)
        self.status = STATUS.IDLE

    def create_parser(self):
        parser = OptionParser(option_list=self.option_list)
        parser.set_usage(self.help)
        self.add_arguments(parser)
        return parser

    def add_arguments(self, parser):
        pass

    def run(self):
        parser = self.create_parser()
        options, args = parser.parse_args()

        if options.NAME and 'unknown' in self.name:
            self.name = options.NAME
        if options.DESCRIPTION:
            self.description = options.DESCRIPTION

        self.process_args_and_options(args, options)

        store(
            data_class='ServiceStart',
            data=dict(
                host=self.host,
                ip=self.ip,
                name=self.name,
                description=self.description
            )
        )

        try:
            self.execute(args, options)
        except KeyboardInterrupt:
            self.terminate()

    def terminate(self):
        self.set_status(STATUS.TERMINATED)
        print("Terminate service {} ".format(self.name))
        sys.exit(0)

    def execute(self, args, options):
        raise NotImplementedError()

    def print_help(self):
        parser = self.create_parser()
        parser.print_help()

    def set_status(self, status):
        if isinstance(status, str):
            status = STATUS[status]
        if self.status_document is None:
            self.status_document = store(
                data_class='ServiceStatus',
                data=dict(
                    host=self.host,
                    ip=self.ip,
                    name=self.name,
                    status=self.status.name,
                    description=self.description
                )
            )
        self.status = status
        self.status_document.status = self.status.name
        self.status_document.create_time = datetime.now()
        self.status_document.save()

    def process_args_and_options(self, args, options):
        pass

    def log(self, msg="", level=logging.INFO):
        logging.log(msg=msg, level=level)
        print(msg)


class UmanoServerService(UmanoService, ABC):
    option_list = UmanoService.option_list + [
        make_option(
            '--port',
            dest='PORT',
            type=int,
            default=5000,
            help='port to listen to (default 5000)'
        ),
        make_option(
            '--host',
            dest='HOST',
            type=str,
            default="0.0.0.0",
            help='ip to bind to (default "0.0.0.0")'
        ),
    ]


class ConsumerService(UmanoService):
    def __init__(self, data_class="TestData") -> None:
        super().__init__()
        self.data_class = data_class
        self.connection = get_connection()
        self.queue = get_queue_for_dataclass(data_class=self.data_class)
        self.consumer = Consumer(self.connection, queues=self.queue, callbacks=[self.process_message], accept=['json'])
        self.consumer.consume()

    def establish_connection(self):
        revived_connection = self.connection.clone()
        revived_connection.ensure_connection(max_retries=3)
        channel = revived_connection.channel()
        self.consumer.revive(channel)
        self.consumer.consume()
        return revived_connection

    def execute(self, args, options):
        self.process_args_and_options(args, options)
        while True:
            try:
                self.consume()
            except self.connection.connection_errors:
                self.log(msg="connection revived")

    def consume(self):
        connection = self.establish_connection()
        while True:
            try:
                connection.drain_events(timeout=0.5)
            except socket.timeout:
                connection.heartbeat_check()

    def process_message(self, body, message):
        self.log(msg="Message received: {}".format(body))
        message.ack()


class DataFetcher(UmanoService):
    option_list = UmanoService.option_list + [
        make_option(
            '--timeout',
            dest='TIMEOUT',
            type=int,
            default=10,
            help='Data fetch frequency in seconds (default 10)'
        ),
    ]

    def __init__(self, data_class="TestData", timeout=10) -> None:
        self.timeout = timeout
        self.data_class = data_class
        self.data = []
        self.last_update = datetime.now() - timedelta(days=60)
        super().__init__()

    def fetch_data(self):
        self.data = updated_after(
            self.data_class,
            self.last_update
        )
        self.last_update = datetime.now()

    def process_data(self):
        pass

    def execute(self, args, options):
        self.process_args_and_options(args, options)
        while True:
            try:
                self.fetch_data()
                self.process_data()
                time.sleep(self.timeout)
            except KeyboardInterrupt:
                raise KeyboardInterrupt
