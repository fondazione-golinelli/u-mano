import cv2
import datetime
import sys
import time

from umano.onehand.utils import VideoGrabber
from umano.onehand.handfeatures.extractor import HandFeatureExtractor
from umano.onehand.utils import rescale_frame
from umano.onehand.osc import send_to_max
from umano.onehand.models import HandFeature
VIDEO_SRC = 0  # "http://localhost:5000/video_feed"

MAX_TIMEOUT = 20

frame_processed = 0

if __name__ == '__main__':

    frame_processed = 0
    index = 0
    num_frames = 0
    fps = 0
    live_output = True

    # video_capture = cv2.VideoCapture(VIDEO_SRC)

    extractor = HandFeatureExtractor(live_output=False)

    start_time = datetime.datetime.now()

    while True:

        frame = VideoGrabber(VIDEO_SRC).grab()
        index += 1
        num_frames += 1

        image_points, output_frame = extractor.process_frame(frame)

        elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
        fps = num_frames // elapsed_time

        print("frame ", index, num_frames, elapsed_time, fps)

        if image_points is not None:
            print("hand detected")
            hand = HandFeature(image_points=image_points)
            send_to_max(hand, all=True)
            time.sleep(10)

            if output_frame is not None and live_output:
                cv2.putText(output_frame, str(int(fps)), (20, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.75, (77, 255, 9), 2)
                cv2.imshow('live', rescale_frame(output_frame, wpercent=50, hpercent=50))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    # video_capture.release()
    sys.exit(0)
