import os
from collections import Counter

import numpy as np
import cv2

from umano.manosola.utils import annotate_frame_with_features
from umano.manosola.settings import HAND_MODEL_URL


class HandFeatureExtractor(object):

    def __init__(self, threshold=0.2, confidence=0.75, live_output=True):
        model_directory = os.path.join(os.path.dirname(__file__), "models")
        proto_file = os.path.join(model_directory, "pose_deploy.prototxt")
        weights_file = os.path.join(model_directory, "pose_iter_102000.caffemodel")

        if not os.path.exists(weights_file):
            raise RuntimeError(
                "Please download hand model from {} and copy it into manosola/handfeatrures/models folder".format(
                    HAND_MODEL_URL))

        self.threshold = threshold
        self.net = cv2.dnn.readNetFromCaffe(proto_file, weights_file)
        self.input_height = 368
        self.points_number = 22
        self.live_output = live_output
        self.confidence = confidence

    def process_frame(self, frame, denoise=False):
        if denoise:
            processed_frame = cv2.GaussianBlur(np.copy(frame), (51, 11), 0)
        else:
            processed_frame = np.copy(frame)

        frame_width = frame.shape[1]
        frame_height = frame.shape[0]
        aspect_ratio = frame_width / frame_height
        input_width = int(((aspect_ratio * self.input_height) * 8) // 8)
        input_blob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (input_width, self.input_height), (0, 0, 0), swapRB=False,
                                           crop=False)
        self.net.setInput(input_blob)
        output = self.net.forward()
        points = []

        for i in range(self.points_number):
            # confidence map of corresponding body's part.
            probability_map = output[0, i, :, :]
            probability_map = cv2.resize(probability_map, (frame_width, frame_height))

            # Find global maxima of the probability_map.
            min_val, prob, min_loc, point = cv2.minMaxLoc(probability_map)

            if prob > self.threshold:
                # cv2.circle(processed_frame, (int(point[0]), int(point[1])), 8, (0, 255, 255), thickness=-1,
                #            lineType=cv2.FILLED)
                cv2.putText(processed_frame, "{}".format(i),
                            (int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 0, 0),
                            2, lineType=cv2.LINE_AA)

                # Add the point to the list if the probability is greater than the threshold
                points.append((int(point[0]), int(point[1])))
            else:
                points.append(None)

        if not self.hand_features_confidence(points):
            return None, processed_frame

        processed_frame = annotate_frame_with_features(processed_frame, points=points)

        if self.live_output:
            # TODO save frame somewhere
            pass

        return points, processed_frame

    def hand_features_confidence(self, features):
        mandatory_points = [0, 1, 2, 5, 9, 13]
        for idx in mandatory_points:
            if features[idx] is None:
                return False
        return Counter(features).get(None, 0) < self.points_number * (1 - self.confidence)
