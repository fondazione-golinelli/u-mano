import importlib
import pyclbr

from umano.hal.exceptions import HalException

CLASSES = [k for k, v in pyclbr.readmodule("umano.hal.models").items() if isinstance(v, pyclbr.Class)]


def class_from_classname(classname):
    if classname not in CLASSES:
        raise HalException()
    return getattr(importlib.import_module("umano.hal.models"), classname)
