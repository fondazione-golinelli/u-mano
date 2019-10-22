import os
import sys
import requests
import json

import shutil

from umano.onehand.models import HandFeature
from umano.onehand.osc import send_to_max

ONEHAND_URL = "http://localhost:5000/onehand"
MAX_OR_VUO_HOST = "127.0.0.1"
MAX_OR_VUO_PORT = 8888
DOWNLOAD_FOLDER = "C:\\Users\\u-man\\Projects\\Hands\\temp"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.mkdir(DOWNLOAD_FOLDER)

if __name__ == "__main__":
    while True:

        r = requests.get(ONEHAND_URL)
        if r.status_code == 200:
            hand_json = json.loads(r.content)
            hand_image_src = hand_json['src']

            response = requests.get(hand_json['url'], stream=True)
            output_path = os.path.join(DOWNLOAD_FOLDER, hand_json['src'])
            with open(output_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

            print("Loaded image features {}".format(hand_image_src))
            print("Image available at {}".format(output_path))
            hand = HandFeature(image_points=hand_json['image_points'])

            send_to_max(hand, host=MAX_OR_VUO_HOST, port=MAX_OR_VUO_PORT)

            key = input("\t Press a key to load another hand, q to exit")
            if key == "q":
                sys.exit(0)

        else:
            print("ERROR CONNECTING TO {}".format(ONEHAND_URL))
            sys.exit(-1)
