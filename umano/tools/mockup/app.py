import os
import argparse
import random

from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify, make_response

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/umano"
mongo = PyMongo(app)


IMAGE_BASE_URL = "https://umano.fondazionegolinelli.it/static/"


@app.route("/onehand")
def onehand():
    howmany_hands = mongo.db.onehand.data.estimated_document_count()
    doc_id = random.randint(0, howmany_hands-1)
    hand = mongo.db.onehand.data.find().skip(doc_id).limit(1)[0]
    hand.pop("_id")
    hand['url'] = os.path.join(IMAGE_BASE_URL, hand['src'])
    res = make_response(jsonify(hand), 200)
    return res


def main(config):
    app.config.update(config)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--host',
        dest='host',
        type=str,
        default="0.0.0.0",
        help='host to bind to (default 0.0.0.0)')
    parser.add_argument(
        '-p',
        '--port',
        dest='port',
        type=int,
        default=5000,
        help='port to listen to (default 5000)')

    args = parser.parse_args()

    app.run(args.host, port=args.port, threaded=True)
