import os
import sys
import requests
import json
import cv2
import shutil

# HACK for easy terminal execution
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
)
# HACK for easy terminal execution

from umano.onehand.models import HandFeature
from umano.onehand.osc import send_to_max, send_to_vuo
from umano.onehand.utils import rescale_frame, annotate_frame_with_features
from umano import settings

if not os.path.exists(settings.ONEHAND_MOCKUP_DOWNLOAD_FOLDER):
    os.mkdir(settings.ONEHAND_MOCKUP_DOWNLOAD_FOLDER)

if __name__ == "__main__":
    while True:

        r = requests.get(settings.ONEHAND_MOCKUP_URL)
        if r.status_code == 200:
            hand_json = json.loads(r.content)
            hand_image_src = hand_json['src']

            response = requests.get(hand_json['url'], stream=True)
            output_path = os.path.join(settings.ONEHAND_MOCKUP_DOWNLOAD_FOLDER, hand_json['src'])
            with open(output_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

            print("\nLoaded image features {}".format(hand_image_src))
            print("Image available at {}\n".format(output_path))
            hand = HandFeature(image_points=hand_json['image_points'])
            print(hand.beats)
            print(hand.attacks)
            print(hand.releases)

            cv2.imshow(output_path,
                       rescale_frame(annotate_frame_with_features(cv2.imread(output_path), hand=hand), wpercent=50,
                                     hpercent=50))

            send_to_max(hand, host=settings.ONEHAND_MAX_HOST, port=settings.ONEHAND_MAX_PORT)
            send_to_vuo(hand, host=settings.ONEHAND_VUO_HOST, port=settings.ONEHAND_VUO_PORT)

            while True:
                print("\n\t - ESC to quit \n\t - SPACEBAR send OSC again\n\t - any other key load a different hand")
                key = cv2.waitKey(0)
                print(key)
                if key == 27:
                    sys.exit(0)
                elif key == 32:
                    send_to_max(hand, host=settings.ONEHAND_MAX_HOST, port=settings.ONEHAND_MAX_PORT)
                    send_to_vuo(hand, host=settings.ONEHAND_VUO_HOST, port=settings.ONEHAND_VUO_PORT)
                    print("\n\t osc sent...")
                elif key == ord('r'):
                    hand.reverse()
                    send_to_max(hand, host=settings.ONEHAND_MAX_HOST, port=settings.ONEHAND_MAX_PORT)
                else:
                    cv2.destroyAllWindows()
                    break

        else:
            print("ERROR CONNECTING TO {}".format(settings.ONEHAND_MOCKUP_URL))
            sys.exit(-1)
