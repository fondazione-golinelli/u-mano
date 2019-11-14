import os
import sys
import random
import time
import cv2


from umano.onehand.models import HandFeature
from umano.onehand.handfeatures.extractor import HandFeatureExtractor
from umano.onehand.utils import rescale_frame, annotate_frame_with_features
from umano.onehand.osc import send_sonification_to_max


if __name__ == "__main__":

    def usage():
        print("\t - ESC to quit \n\t - d only durer \n\t - h only hand \n\t - w all freq \t\n - any other key next")

    TEST_DIRECTORY = "C:\\Users\\u-man\\Projects\\Hands\\processed"

    extractor = HandFeatureExtractor(live_output=False)

    random_image = False
    # timer = None
    # timeout = 10

    for file_name in os.listdir(TEST_DIRECTORY):

        image_path = os.path.join(TEST_DIRECTORY, file_name)
        print("- processing image {}".format(image_path))
        if random_image and random.randint(0, 100) < 75:
            print("\t - skip")
            continue

        if '_processed' in file_name:
            continue

        frame = cv2.imread(image_path)
        frame_copy = frame.copy()

        image_points, processed_frame = extractor.process_frame(frame_copy)
        if image_points is None:
            cv2.imshow(file_name, rescale_frame(processed_frame))
            cv2.waitKey(0)
            cv2.destroyWindow(file_name)
            image_points, processed_frame = extractor.process_frame(frame_copy, denoise=True)
            if image_points is None:
                cv2.imshow(file_name, rescale_frame(processed_frame))
                cv2.waitKey(0)
                continue

        # timer = time.time()

        hand = HandFeature(image_points=image_points, source_image=image_path)
        cv2.imshow(file_name, rescale_frame(annotate_frame_with_features(frame_copy, hand=hand)))
        send_sonification_to_max(hand, all=True)

        while True:
            usage()
            key = cv2.waitKey(1)

            # if time.time() > (timer + timeout):
            #     print("timeout")
            #     cv2.destroyAllWindows()
            #     break

            time.sleep(20)
            if key == 27:
                cv2.destroyAllWindows()
                sys.exit(0)
            elif key == ord("w"):
                send_sonification_to_max(hand, all=True)
            elif key == ord("d"):
                send_sonification_to_max(hand, all=False, only_durer=True)
            elif key == ord("h"):
                send_sonification_to_max(hand, all=False, only_hand=True)
            elif key == ord("s"):
                cv2.imwrite(
                    os.path.join(TEST_DIRECTORY, "{}_processed.jpg".format(file_name)),
                    annotate_frame_with_features(processed_frame, hand=hand)
                )
            else:
                cv2.destroyAllWindows()
                break
