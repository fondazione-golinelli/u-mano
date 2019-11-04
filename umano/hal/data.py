from datetime import datetime
from dacite import from_dict

from bson import ObjectId

from umano.hal.messages import publish
from umano.hal.utils import class_from_classname


def create(data_class, data):
    if isinstance(data_class, str):
        data_class = class_from_classname(data_class)
    default = dict(
        create_time=datetime.now(),
        score=.0,
        likes=0
    )
    default.update(data)

    return from_dict(data_class=data_class, data=default)


def store(instance=None, data_class=None, data=None, publish_after=True):
    if instance is None:
        if isinstance(data_class, str):
            data_class = class_from_classname(data_class)
        instance = create(data_class, data)
    instance.save()

    if publish_after:
        publish(instance)

    return instance


def load(pk, data_class):
    if isinstance(data_class, str):
        data_class = class_from_classname(data_class)
    data = data_class.get_collection().find_one({"_id": ObjectId(pk)})
    return create(data_class, data)


def find(data_class, query):
    if isinstance(data_class, str):
        data_class = class_from_classname(data_class)
    documents = []
    cursor = data_class.get_collection().find(query)
    for data in cursor:
        documents.append(
            create(data_class, data)
        )
    return documents


def updated_after(data_class, update_time):
    return find(data_class, {"create_time": {"$gte": update_time}})


def last(data_class, query=None):
    if isinstance(data_class, str):
        data_class = class_from_classname(data_class)
    try:
        if query is None:
            query = dict()
        return create(data_class, data_class.get_collection().find(query).sort("create_time", direction=-1).limit(1)[0])
    except IndexError:
        return None
