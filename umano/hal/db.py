import os
from pymongo import MongoClient

from umano import settings
client = MongoClient(settings.HAL_MONGODB_URL)
database = client.umano
