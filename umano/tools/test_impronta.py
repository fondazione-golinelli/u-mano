import sys
import cv2
import imutils
import numpy as np
from skimage.measure import compare_ssim

from onehand.utils import rescale_frame
from umano.onehand.utils import VideoGrabber, rescale_frame


class BigG(object):

    def __init__(self, delta=0.01, camera=0) -> None:
        super().__init__()
        self.average_frame = None
        self.background_mask = None
        self.video_source = camera
        self.capture = cv2.VideoCapture(self.video_source)
        self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
        self.background_subtractor = cv2.createBackgroundSubtractorMOG2(100, 2, True)

        self.average_frame = None
        self.delta = delta
        self.processed_frames = 0
        self.background_init = 100

    def run(self):
        while True:
            try:
                self.process_frame()
            except KeyboardInterrupt:
                self.capture.release()
                cv2.destroyAllWindows()
                sys.exit(0)

    def process_frame(self):

        _, frame = self.capture.read()

        if self.processed_frames < self.background_init:
            if self.average_frame is None:
                self.average_frame = np.float32(frame)
            self.average_frame = cv2.accumulateWeighted(cv2.GaussianBlur(frame, (11, 11), 0), self.average_frame, self.delta)
            self.processed_frames += 1
            return

        background_mask = self.background_subtractor.apply(cv2.GaussianBlur(frame, (11, 11), 0))
        background_mask = cv2.morphologyEx(background_mask, cv2.MORPH_OPEN, self.kernel)

        # cv2.accumulateWeighted(frame, self.average_frame, self.delta)
        # cv2.imshow("live", rescale_frame(frame))
        cv2.imshow("bg", rescale_frame(background_mask))
        cv2.waitKey(1)

    # @staticmethod
    # def compute_diff(imageA, imageB):
    #
    #     max_w, max_h = None, None
    #     if imageA.shape[:2] != imageB.shape[:2]:
    #         max_w = max(imageA.shape[0], imageB.shape[0])
    #         max_h = max(imageA.shape[1], imageB.shape[1])
    #
    #     # convert the images to grayscale
    #     if max_w or max_h:
    #         grayA = cv2.cvtColor(
    #             imutils.resize(imageA, width=max_w, height=max_h), cv2.COLOR_BGR2GRAY)
    #         grayB = cv2.cvtColor(
    #             imutils.resize(imageB, width=max_w, height=max_h), cv2.COLOR_BGR2GRAY)
    #         if grayA.shape != grayB.shape:
    #             gray_max_w = max(grayA.shape[0], grayB.shape[0])
    #             gray_max_h = max(grayA.shape[1], grayB.shape[1])
    #             right_a, bottom_a = gray_max_h-grayA.shape[1],  gray_max_w-grayA.shape[0]
    #             right_b, bottom_b = gray_max_h-grayB.shape[1],  gray_max_w-grayB.shape[0]
    #             if (bottom_a, right_a) != (0, 0):
    #                 grayA = cv2.copyMakeBorder(
    #                     grayA, 0, bottom_a, 0, right_a,
    #                     cv2.BORDER_CONSTANT, value=(0, 0, 0))
    #             if (bottom_b, right_b) != (0, 0):
    #                 grayB = cv2.copyMakeBorder(
    #                     grayB, 0, bottom_b, 0, right_b,
    #                     cv2.BORDER_CONSTANT, value=(0, 0, 0))
    #     else:
    #         grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    #         grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    #
    #     # compute the Structural Similarity Index (SSIM) between the two
    #     # images, ensuring that the difference image is returned
    #     (score, diff) = compare_ssim(
    #         cv2.GaussianBlur(np.copy(grayA), (51, 11), 0),
    #         cv2.GaussianBlur(np.copy(grayB), (51, 11), 0), full=True)
    #     diff = (diff * 255).astype("uint8")
    #     # print("SSIM: {}".format(score))
    #
    #     # threshold the difference image, followed by finding contours to
    #     # obtain the regions of the two input images that differ
    #     thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #     # cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #     # cnts = imutils.grab_contours(cnts)
    #     #
    #     # # loop over the contours
    #     # for c in cnts:
    #     #     # compute the bounding box of the contour and then draw the
    #     #     # bounding box on both input images to represent where the two
    #     #     # images differ
    #     #     (x, y, w, h) = cv2.boundingRect(c)
    #     #     cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #     #     cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #
    #     # show the output images using cv2
    #     cv2.imshow("Diff", rescale_frame(diff))
    #     cv2.imshow("Thresh", rescale_frame(thresh))
    #     return diff


if __name__ == "__main__":
    bb = BigG()
    bb.run()
