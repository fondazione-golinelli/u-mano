import os
import cv2
from umano.manosola.utils import annotate_frame_with_features


def durerizer(LL):
    L19 = LL / 19
    C = LL
    K = LL - L19 * 7
    H = LL - L19 * 1.5
    I = LL - L19 * 4
    G = LL - L19 * 1
    N = LL - L19 * 14
    O = LL - L19 * 10
    P = LL - L19 * 6
    L = M = LL - L19 * 11

    KN = abs(K - N)
    CP = abs(C - P)
    HL = abs(H - L)
    KG = abs(K - G)

    hand_width = L19 * 11
    middle_finger_width = abs(M - C) / 5
    index_finger_width = middle_finger_width * 4 / 5

    points = [(0.0, 0.0)] * 21

    # thumb
    # il punto 1 non esiste in Durer, interpolo
    points[2] = (-hand_width / 2 + KN / 4, N)
    points[1] = ((points[0][0] + points[2][0]) * 0.5, (points[0][1] + points[2][1]) * 0.5)
    points[3] = (-hand_width / 2 + KN / 4, O)
    points[4] = (-hand_width / 2, K)

    # index finger
    points[5] = (- middle_finger_width / 2 - index_finger_width / 2, M)
    points[6] = (- middle_finger_width / 2 - index_finger_width / 2, H - HL / 2 * 7 / 7)
    points[7] = (- middle_finger_width / 2 - index_finger_width / 2 * 4 / 5, H - HL / 2 * 3 / 7)
    points[8] = (- middle_finger_width / 2 - index_finger_width / 2 * 4 / 5, H)

    # middle finger
    points[9] = (0, M)
    points[10] = (0, P)
    points[11] = (0, C - CP * 3 / 7)
    points[12] = (0, C)

    middle_finger_half_height = points[11][1] - points[9][1]

    # ring finger
    # HACK! Durer non è stato molto chiaro per la nocca dell'anulare, devo interpolare
    ring_finger_lower_article = M - (M - (I - middle_finger_half_height)) / 2
    ring_finger_width = abs(G - ring_finger_lower_article) / 5
    points[13] = (middle_finger_width / 2 + ring_finger_width / 2, ring_finger_lower_article)
    points[14] = (middle_finger_width / 2 + ring_finger_width / 2, K)
    points[15] = (middle_finger_width / 2 + ring_finger_width / 2 * 3 / 4, G - KG * 4 / 9)
    points[16] = (middle_finger_width / 2 + ring_finger_width / 2 * 3 / 4, G)

    # little finger
    little_finger_width = middle_finger_half_height / 5
    points[17] = (middle_finger_width / 2 + ring_finger_width + little_finger_width / 2, I - middle_finger_half_height)
    points[18] = (middle_finger_width / 2 + ring_finger_width + little_finger_width / 2,
                  I - middle_finger_half_height * 6 / 11)
    points[19] = (middle_finger_width / 2 + ring_finger_width + little_finger_width / 2 * 3 / 4,
                  I - middle_finger_half_height * 6 / 11 * 6 / 11)
    points[20] = (middle_finger_width / 2 + ring_finger_width + little_finger_width / 2 * 3 / 4, I)

    return [(int(x), int(y)) for x, y in points]


if __name__ == "__main__":
    img = cv2.imread(os.path.join(os.path.dirname(__file__), "durer_sample.png"))

    # translate points to hand origin in image
    origin = (635, 675)
    h = 590  # height in pixel of hand in durer
    points = [(int(x) + int(origin[0]), int(origin[1]) - int(y)) for x, y in durerizer(h)]
    cv2.imshow('durer in the machine (any key to close)', annotate_frame_with_features(img, points=points))

    key = cv2.waitKey(0)
    cv2.destroyAllWindows()