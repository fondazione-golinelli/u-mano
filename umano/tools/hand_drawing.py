import os
import sys
import cv2
import numpy as np

from umano.onehand.utils import rescale_frame, denoise, rgb_histogram, hand_print, hand_roi, crop
from umano.hal.data import find

for hp in find(data_class="OneHandPicture", query={}):

    if not os.path.exists(hp.src):
        continue

    frame = cv2.imread(hp.src)
    mask = hand_print(hp, frame.shape[0], frame.shape[1])
    cv2.imshow("hand print", rescale_frame(mask))

    min_xy, max_xy = hand_roi(hp)

    mask = crop(mask, min_xy, max_xy)
    cropped_image = denoise(crop(frame, min_xy, max_xy))

    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    masked_image = cv2.bitwise_and(cropped_image, cropped_image, mask=mask)
    cv2.imshow("masked", rescale_frame(masked_image))
    cv2.imshow("histogram", rgb_histogram(cropped_image))

    bgr = cv2.split(cropped_image)
    COLORS = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255)
    ]
    for i, img in enumerate(bgr):
        print(i)
        min_level = np.min(img)
        max_level = np.max(img)
        print(min_level, max_level)
        ret, thresh = cv2.threshold(img, 50, max_level, 0)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)

        for c in contours:
            cv2.drawContours(cropped_image, [c], 0, COLORS[i], 3)

    cv2.imshow("crop", cropped_image)

    cv2.waitKey(0)

cv2.destroyAllWindows()
