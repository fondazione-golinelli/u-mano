import cv2
import numpy as np

from umano.onehand.utils import rescale_frame, HANDPOINT_PAIRS
from umano.hal.data import last, find

for hp in find(data_class="OneHandPicture", query={}):

    frame = cv2.imread(hp.src)
    black = np.zeros(frame.shape)
    WHITE = (255, 255, 255)

    # detect roi of image
    min_xy = [1000, 1000]
    max_xy = [0, 0]

    for idx, pair in enumerate(HANDPOINT_PAIRS):
        part_a = pair[0]
        part_b = pair[1]

        if hp.image_points[part_a] and hp.image_points[part_b]:
            cv2.line(frame, tuple(hp.image_points[part_a]), tuple(hp.image_points[part_b]), WHITE, 20)
            cv2.circle(frame, tuple(hp.image_points[part_a]), 10, (255, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.circle(frame, tuple(hp.image_points[part_b]), 10, (255, 255, 255), thickness=-1, lineType=cv2.FILLED)



        vertices = np.array([[
            hp.image_points[0],
            hp.image_points[2],
            hp.image_points[5],
            hp.image_points[9],
            hp.image_points[13],
            hp.image_points[17],

        ]], np.int32)
        cv2.polylines(frame, vertices, True, WHITE, thickness=20, lineType=cv2.FILLED)

    cv2.imshow("original", frame)
    # cv2.imshow("black", black)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
