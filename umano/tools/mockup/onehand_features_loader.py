import cv2
import os

from umano.hal.data import store
from umano.hal.models import OneHandPicture

from umano.onehand.handfeatures.extractor import HandFeatureExtractor
from umano.onehand.utils import rescale_frame

IMAGES_DIRECTORY = "C:\\Users\\u-man\\Projects\\Hands\\processed"

extractor = HandFeatureExtractor(
    live_output=False
)

for filename in os.listdir(IMAGES_DIRECTORY):
    src_image = os.path.join(IMAGES_DIRECTORY, filename)
    frame = cv2.imread(src_image)
    frame_copy = frame.copy()
    image_points, processed_frame = extractor.process_frame(frame_copy)
    cv2.imshow('hand feature keypoints + skeleton', rescale_frame(processed_frame))

    print("processed image {}".format(src_image))
    if image_points is None:
        continue

    data = dict(
        src=filename,
        hand=True,
        image_points=image_points,
        features=""
    )

    store(data_class=OneHandPicture, data=data, publish_after=False)

    if extractor.live_output:
        key = cv2.waitKey(0)



        if key == 27:
            cv2.destroyAllWindows()
            break
        else:
            continue
