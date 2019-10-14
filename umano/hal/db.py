import os
from pymongo import MongoClient

client = MongoClient(os.environ.get("MONGODB_URL", 'mongodb://localhost:27017/'))
database = client.umano
