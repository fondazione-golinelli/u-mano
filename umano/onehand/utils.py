from datetime import datetime
from math import log2, pow
from statistics import mean, StatisticsError
import string
import tempfile
import time


import numpy as np
import cv2
from scipy.spatial import distance as dist

from pythonosc import udp_client

from umano import settings

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
    try:
        d = dist.euclidean((point_a[0], point_a[1]), (point_b[0], point_b[1]))
        return d
    except TypeError:
        return 0


def pixels_to_frequency(pixels, reference_length, reference_frequency):
    return wavelength_to_frequency(pixels * frequency_to_wavelength(reference_frequency) / reference_length)


def frequency_to_wavelength(f):
    return SPEED_OF_SOUND / f


def wavelength_to_frequency(l):
    return SPEED_OF_SOUND / l


def frequency_to_note(f, A4=432):
    C0 = A4 * pow(2, -4.75)
    name = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    h = round(12 * log2(f / C0))
    octave = h // 12
    n = h % 12
    return "{}_{}".format(name[n], str(octave))


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
            distances.append(round(distance))
        else:
            frequencies.append(0)
            distances.append(0)

    return frequencies, distances, hand_length


def annotate_frame_with_features(frame, points=None, hand=None):
    if points is None and hand is None:
        raise RuntimeError("hand or points required")
    COLORS = [
        (255, 0, 255),
        (0, 255, 0),
        (0, 128, 255),
        (0, 0, 255),
        (255, 0, 0),
    ]
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    BLACK = (0, 0, 0)

    if points is None:
        points = hand.image_points

    color_index = -1
    for idx, pair in enumerate(HANDPOINT_PAIRS):
        part_a = pair[0]
        part_b = pair[1]
        if idx % 4 == 0:
            color_index += 1

        if points[part_a] and points[part_b] and None not in points[part_a] and None not in points[part_b]:
            cv2.line(frame, tuple(points[part_a]), tuple(points[part_b]), COLORS[color_index], 2)
            cv2.circle(frame, tuple(points[part_a]), 10, (255, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.circle(frame, tuple(points[part_b]), 10, (255, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frame, str(part_a), tuple(points[part_a]), cv2.FONT_HERSHEY_SIMPLEX, 0.55, BLACK, 2)
            cv2.putText(frame, str(part_b), tuple(points[part_b]), cv2.FONT_HERSHEY_SIMPLEX, 0.55, BLACK, 2)

            mx, my = midpoint(points[part_a], points[part_b])
            d = compute_distance(points[part_a], points[part_b])
            if hand is not None:
                text = "{:.1f} Hz".format(pixels_to_frequency(d, hand.hand_length, hand.reference_frequency))
            else:
                text = "{:.1f}".format(d)
            cv2.putText(frame, text, (int(mx), int(my - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, GRAY, 2)

    if hand is not None:
        color_index = -1
        print(frame.shape)
        x = round(frame.shape[0] / 10)
        y = frame.shape[1] - round(frame.shape[1] / 3)
        max_x = frame.shape[0] - round(frame.shape[0] / 10)

        mx = max_x + x
        mt = max(hand.beats) + max(hand.releases) + max(hand.attacks)
        dy = 100
        yy = y

        def time_to_pixel(t):
            return int(round(mx * t / mt) + x)

        for idx, b in enumerate(hand.beats):
            if idx % 4 == 0:
                color_index += 1
                yy = y + 25 * color_index
                cv2.line(frame, (x, yy), (mx, yy), GRAY, 2)
            yy = y + 25 * color_index

            # vertices = np.array([[
            #     (time_to_pixel(b), yy),
            #     (time_to_pixel(b) + time_to_pixel(hand.attacks[idx]), yy - dy),
            #     (time_to_pixel(b) + time_to_pixel(hand.attacks[idx]) + time_to_pixel(hand.releases[idx]), yy)
            # ]], np.int32)
            # cv2.polylines(frame, vertices, True, COLORS[color_index], 3)

            cv2.circle(frame, (time_to_pixel(b), yy), 5, COLORS[color_index], thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frame, str(idx), (time_to_pixel(b), yy), cv2.FONT_HERSHEY_SIMPLEX, 0.55, GRAY, 2)

    return frame


class VideoGrabber(object):

    def __init__(self, video_source=None):
        if isinstance(video_source, str) and video_source in string.digits:
            self.video_source = int(video_source)
        else:
            self.video_source = video_source

    def grab(self):
        capture = cv2.VideoCapture(self.video_source)
        if capture.isOpened():
            _, frame = capture.read()
            capture.release()
            return frame
        return None


def average_points(images):
    points = []
    for i in range(21):
        try:
            x = round(mean([p.image_points[i][0] for p in images if p.image_points[i] is not None]))
        except StatisticsError:
            x = None
        try:
            y = round(mean([p.image_points[i][1] for p in images if p.image_points[i] is not None]))
        except StatisticsError:
            y = None
        points.append([x, y])
    return points


def temporary_name(with_timestamp=True):
    temp_name = next(tempfile._get_candidate_names())
    if with_timestamp:
        return "{}_{}".format(datetime.now().strftime("%Y_%m_%d__%H_%M_%S_%f"), temp_name)
    return temp_name


def rgb_histogram(image):
    bgr_planes = cv2.split(image)
    hist_size = 256
    hist_range = (0, 256)  # the upper boundary is exclusive
    accumulate = False

    b_hist = cv2.calcHist(bgr_planes, [0], None, [hist_size], hist_range, accumulate=accumulate)
    g_hist = cv2.calcHist(bgr_planes, [1], None, [hist_size], hist_range, accumulate=accumulate)
    r_hist = cv2.calcHist(bgr_planes, [2], None, [hist_size], hist_range, accumulate=accumulate)
    hist_w = 512
    hist_h = 400
    bin_w = int(round(hist_w / hist_size))

    hist_image = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

    cv2.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)

    for i in range(1, hist_size):
        cv2.line(hist_image, (bin_w * (i - 1), hist_h - int(b_hist[i - 1].round())),
                 (bin_w * i, hist_h - int(b_hist[i].round())),
                 (255, 0, 0), thickness=2)
        cv2.line(hist_image, (bin_w * (i - 1), hist_h - int(g_hist[i - 1].round())),
                 (bin_w * i, hist_h - int(g_hist[i].round())),
                 (0, 255, 0), thickness=2)
        cv2.line(hist_image, (bin_w * (i - 1), hist_h - int(r_hist[i - 1].round())),
                 (bin_w * i, hist_h - int(r_hist[i].round())),
                 (0, 0, 255), thickness=2)

    return hist_image


def hand_print(hp, x, y):

    handprint = np.zeros([x, y], np.uint8)

    white = (255, 255, 255)

    for idx, pair in enumerate(HANDPOINT_PAIRS):
        part_a = pair[0]
        part_b = pair[1]

        if hp.image_points[part_a] and hp.image_points[part_b]:
            cv2.line(handprint, tuple(hp.image_points[part_a]), tuple(hp.image_points[part_b]), white, 40)
            cv2.circle(handprint, tuple(hp.image_points[part_a]), 20, white, thickness=-1)
            cv2.circle(handprint, tuple(hp.image_points[part_b]), 20, white, thickness=-1)

        vertices = np.array([[
            hp.image_points[0],
            hp.image_points[2],
            hp.image_points[5],
            hp.image_points[9],
            hp.image_points[13],
            hp.image_points[17],

        ]], np.int32)
        cv2.fillPoly(handprint, vertices, white)

    return handprint


def hand_roi(hand, offset=100):
    min_xy = (
        min([p[0] for p in hand.image_points if p is not None and p[0] is not None]) - offset,
        min([p[1] for p in hand.image_points if p is not None and p[1] is not None]) - offset,
    )
    max_xy = (
        max([p[0] for p in hand.image_points if p is not None and p[0] is not None]) + offset,
        max([p[1] for p in hand.image_points if p is not None and p[1] is not None]) + offset,
    )
    return min_xy, max_xy


def crop(image, min_xy, max_xy):
    return image[min_xy[1]:max_xy[1], min_xy[0]:max_xy[0]]


def toggle_corridor_light(on=True, steps=25, duration=3.0, max_intensity=255.0):

    client = udp_client.SimpleUDPClient(settings.SUS_MILLUMIN_HOST, settings.SUS_MILLUMIN_PORT)

    intensity = not on and max_intensity or 0.0
    for x in range(steps):
        time.sleep(duration/steps)
        # client.send_message(settings.SUS_OSC_LIGHTS_CORRIDOR_INTENSITY_ADDRESS, intensity)
        intensity = intensity + (on and 1.0 or -1.0) * max_intensity/steps
        print(intensity)


