from kombu import Connection, Exchange, Queue
from umano import settings

from umano.hal.exceptions import HalException

UMANO_EXCHANGE = Exchange(settings.HAL_EXCHANGE_NAME, 'direct', durable=True)


def get_queue_for_dataclass(instance=None, classname=None):
    if instance is not None:
        routing_key = queue_name = str(instance.classname).lower()
    elif classname is not None:
        routing_key = queue_name = str(classname).lower()
    else:
        raise HalException("hal.data.get_queue_routing_key_for_dataclass! one of instance or classname is required")
    return Queue(queue_name, exchange=UMANO_EXCHANGE, routing_key=routing_key)


def publish(instance):
    with Connection(settings.HAL_BROKER_URL) as connection:
        queue = get_queue_for_dataclass(instance)

        producer = connection.Producer(serializer='json')
        data = dict(pk=instance.pk, cls=instance.classname)
        producer.publish(data, exchange=UMANO_EXCHANGE, routing_key=queue.routing_key, declare=[queue])
