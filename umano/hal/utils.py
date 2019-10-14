import importlib


def class_from_classname(classname):
    return getattr(importlib.import_module("umano.hal.models"), classname)
