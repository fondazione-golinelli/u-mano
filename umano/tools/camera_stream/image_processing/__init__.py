import numpy as np
import cv2


class BaseProcessing(object):

    def process_frame(self, frame):
        return frame


class BackgroundSubtraction(BaseProcessing):
    def __init__(self, background_subtractor="MOG2", delta=0.1):
        if background_subtractor == "MOG2":
            self.background_subtractor = cv2.createBackgroundSubtractorMOG2(250)
        elif background_subtractor == "KNN":
            self.background_subtractor = cv2.createBackgroundSubtractorKNN(25)
        self.average_frame = None
        self.delta = delta

    def process_frame(self, frame):
        if self.average_frame is None:
            self.average_frame = np.float32(frame)
        self.average_frame = cv2.accumulateWeighted(frame, self.average_frame, self.delta)
        background_mask = self.background_subtractor.apply(self.average_frame)
        return background_mask
