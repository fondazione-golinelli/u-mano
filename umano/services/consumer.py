import socket

from kombu import Consumer

from umano.hal.messages import get_queue_for_dataclass, get_connection
from umano.services.base import UmanoService


class ConsumerService(UmanoService):
    def __init__(self, data_class="TestData") -> None:
        super().__init__()
        self.connection = get_connection()
        self.queue = get_queue_for_dataclass(data_class=data_class)
        self.consumer = Consumer(self.connection, queues=self.queue, callbacks=[self.process_message], accept=['json'])
        self.consumer.consume()

    def establish_connection(self):
        revived_connection = self.connection.clone()
        revived_connection.ensure_connection(max_retries=3)
        channel = revived_connection.channel()
        self.consumer.revive(channel)
        self.consumer.consume()
        return revived_connection

    def execute(self, *args, **options):
        while True:
            try:
                self.consume()
            except self.connection.connection_errors:
                print("connection revived")

    def consume(self):
        connection = self.establish_connection()
        while True:
            try:
                connection.drain_events(timeout=2)
            except socket.timeout:
                connection.heartbeat_check()

    def process_message(self, body, message):
        print("Message received: {}".format(body))
        message.ack()


if __name__ == "__main__":
    service = ConsumerService(data_class="TestData")
    service.run()
