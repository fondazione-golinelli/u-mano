from math import log2, pow
import cv2
from scipy.spatial import distance as dist

SPEED_OF_SOUND = 344  # m/s in air
HANDPOINT_PAIRS = [
        [0, 1], [1, 2], [2, 3], [3, 4],  # thumb
        [0, 5], [5, 6], [6, 7], [7, 8],  # index
        [0, 9], [9, 10], [10, 11], [11, 12],  # middle
        [0, 13], [13, 14], [14, 15], [15, 16],  # ring
        [0, 17], [17, 18], [18, 19], [19, 20]  # little
    ]


def rescale_frame(frame, wpercent=30, hpercent=30):
    width = int(frame.shape[1] * wpercent / 100)
    height = int(frame.shape[0] * hpercent / 100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


def denoise(frame):
    k = 5
    frame = cv2.medianBlur(frame, k)
    frame = cv2.GaussianBlur(frame, (k, k), 0)
    return frame


def midpoint(point_a, point_b):
    return (point_a[0] + point_b[0]) * 0.5, (point_a[1] + point_b[1]) * 0.5


def compute_distance(point_a, point_b, reference=None):
    d = dist.euclidean((point_a[0], point_a[1]), (point_b[0], point_b[1]))
    return d


def pixels_to_frequency(pixels, reference_length, reference_frequency):
    return wavelength_to_frequency(pixels * frequency_to_wavelength(reference_frequency) / reference_length)


def frequency_to_wavelength(f):
    return SPEED_OF_SOUND / f


def wavelength_to_frequency(l):
    return SPEED_OF_SOUND / l


def frequency_to_note(f, A4=432):
    C0 = A4 * pow(2, -4.75)
    name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    h = round(12 * log2(f / C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)


def points_to_frequencies(image_points, reference_frequency):
    frequencies = []
    distances = []
    hand_length = max(
        [compute_distance(image_points[0], image_points[p2]) for p1, p2 in HANDPOINT_PAIRS if
         image_points[0] and image_points[p2]]
    )
    for p1, p2 in HANDPOINT_PAIRS:
        point_1 = image_points[p1]
        point_2 = image_points[p2]
        if point_1 and point_2:
            distance = compute_distance(point_1, point_2)
            freq = pixels_to_frequency(distance, hand_length, reference_frequency)
            frequencies.append(round(freq, 2))
            distances.append(distance)
        else:
            frequencies.append(0)
            distances.append(0)

    return frequencies, distances, hand_length


def annotate_frame_with_features(frame, points=None, hand=None):

    if points is None and hand is None:
        raise RuntimeError("hand or points required")

    if points is None:
        points = hand.image_points

    for pair in HANDPOINT_PAIRS:
        part_a = pair[0]
        part_b = pair[1]

        if points[part_a] and points[part_b]:
            cv2.line(frame, points[part_a], points[part_b], (0, 255, 255), 2)
            cv2.circle(frame, points[part_a], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.circle(frame, points[part_b], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

            mx, my = midpoint(points[part_a], points[part_b])
            d = compute_distance(points[part_a], points[part_b])
            if hand is not None:
                text = "{:.1f} Hz".format(pixels_to_frequency(d, hand.hand_length, hand.reference_frequency))
            else:
                text = "{:.1f}".format(d)
            cv2.putText(frame, text, (int(mx), int(my - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                        0.55,
                        (255, 0, 0), 2)

    return frame


class VideoGrabber(object):

    def __init__(self, video_source=None):
        self.video_source = video_source

    def grab(self):
        capture = cv2.VideoCapture(self.video_source)
        if capture.isOpened():
            _, frame = capture.read()
            capture.release()
            return frame
        return None