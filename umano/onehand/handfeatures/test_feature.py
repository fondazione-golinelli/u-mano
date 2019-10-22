import csv
import cv2
import os
import random

from umano.onehand.handfeatures.extractor import HandFeatureExtractor
from umano.onehand.utils import rescale_frame, annotate_frame_with_features

TEST_DIRECTORY = "C:\\Users\\u-man\\Projects\\Hands\\"
OUTPUT_DIRECTORY = "C:\\Users\\u-man\\Projects\\Hands\\processed"
TEST_CSV = os.path.join(TEST_DIRECTORY, "HandInfo.csv")

reader = csv.DictReader(open(TEST_CSV, 'r'))

extractor = HandFeatureExtractor(
    live_output=True
)

for row in reader:
    if 'palmar' not in row.get('aspectOfHand'):
        continue

    fname = os.path.join(TEST_DIRECTORY, row.get('imageName'))
    print(fname)
    if os.path.exists(os.path.join(OUTPUT_DIRECTORY, row.get('imageName'))):
        continue
    frame = cv2.imread(fname)
    frame_copy = frame.copy()
    hand_features, processed_frame = extractor.process_frame(frame_copy)
    if hand_features is None:
        continue
    cv2.imwrite(os.path.join(OUTPUT_DIRECTORY, row.get('imageName')), frame)
    print("- image saved!")
    cv2.imshow('hand feature keypoints + skeleton', rescale_frame(processed_frame))

    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()
        break
    else:
        continue

