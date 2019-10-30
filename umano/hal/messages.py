from kombu import Connection, Exchange, Queue
from umano import settings

from umano.hal.exceptions import HalException

UMANO_EXCHANGE = Exchange(settings.HAL_EXCHANGE_NAME, 'direct', durable=True)


def get_queue_for_dataclass(instance=None, data_class=None):
    if instance is not None:
        routing_key = queue_name = str(instance.classname).lower()
    elif data_class is not None:
        routing_key = queue_name = str(data_class).lower()
    else:
        raise HalException("hal.data.get_queue_routing_key_for_dataclass! one of instance or data_class is required")
    return Queue(queue_name, exchange=UMANO_EXCHANGE, routing_key=routing_key)


def get_connection():
    return Connection(settings.HAL_BROKER_URL, heartbeat=5)


def publish(instance):
    with get_connection() as connection:
        queue = get_queue_for_dataclass(instance)

        producer = connection.Producer(serializer='json')
        data = dict(pk=instance.pk, cls=instance.classname)
        producer.publish(data, exchange=UMANO_EXCHANGE, routing_key=queue.routing_key, declare=[queue])
