import os

import cv2
import numpy as np
import logging

from umano.services.base import DataFetcher
from umano.hal.data import last
from umano.onehand.models import HandFeature
from umano.onehand.utils import hand_roi, hand_print, crop, annotate_frame_with_features
from umano import settings


class TheChief(DataFetcher):
    def __init__(self, data_class="OneHandFeatures", timeout=10) -> None:
        super().__init__(data_class, timeout)
        self.name = "The Chief"
        self.description = "Search for new members and get their hand print"

    def process_data(self):
        for hand_feature in self.data:
            self.log(msg="found hand {}".format(hand_feature.uid))
            hand_picture = last("OneHandPicture", query={"touch_session_id": hand_feature.touch_session_id})
            if hand_picture is None:
                continue
            if not os.path.exists(hand_picture.src):
                continue
            try:
                min_xy, max_xy = hand_roi(hand_feature)
                frame = cv2.imread(hand_picture.src)
                handprint = crop(hand_print(hand_picture, frame.shape[0], frame.shape[1]), min_xy, max_xy)

                output_file = os.path.join(
                    settings.ONEHAND_HAND_PRINTS_FOLDER,
                    "{}{}".format(hand_feature.uid, settings.ONEHAND_HAND_PRINTS_EXTENSION)
                )
                cv2.imwrite(output_file, handprint)

                features = np.zeros(shape=frame.shape)
                hand = HandFeature(hand_feature.image_points)
                annotate_frame_with_features(features, hand=hand)
                output_file = os.path.join(
                    settings.ONEHAND_HAND_PRINTS_FOLDER,
                    "{}_features{}".format(hand_feature.uid, settings.ONEHAND_HAND_PRINTS_EXTENSION)
                )
                cv2.imwrite(output_file, crop(features, min_xy, max_xy))
                hand_feature.width = handprint.shape[0]
                hand_feature.height = handprint.shape[1]
                hand_feature.hand_print = True
                hand_feature.save()
                self.log(msg="processed hand {}".format(hand_feature.uid))
            except:
                self.log(msg="critical error with hand {}".format(hand_feature.uid), level=logging.CRITICAL)

if __name__ == "__main__":
    service = TheChief()
    service.run()
