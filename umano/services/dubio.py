import time
from datetime import datetime
from optparse import make_option
import os

import cv2

from umano.services.base import ConsumerService, STATUS
from umano.hal.data import load, store, find, create
from umano.onehand.handfeatures.extractor import HandFeatureExtractor
from umano.onehand.utils import VideoGrabber, average_points, temporary_name
from umano.onehand.models import HandFeature
from umano.onehand.osc import send_to_max
from umano import settings


class DuBio(ConsumerService):
    option_list = ConsumerService.option_list + [
        make_option(
            '--video',
            dest='VIDEO_SOURCE',
            type=str,
            default="0",
            help='video stream to read from (default "0")'
        ),
        make_option(
            '--hands',
            dest='HANDS',
            type=int,
            default=2,
            help='number of images with hand required to proceed with sonification (default 2)'
        ),
    ]

    def __init__(self, data_class="OneHandTouch", hand_data_class="OneHandPicture") -> None:
        super().__init__(data_class)
        self.session_id = None
        self.video_source = None
        self.hand_frames = []
        self.hand_data_class = hand_data_class
        self.hands_to_sonification = None
        self.name = "DuBio"
        self.description = "Extract hand features and trigger sonification"
        self.start_time = None

    def process_args_and_options(self, args, options):
        self.video_source = options.VIDEO_SOURCE
        self.hands_to_sonification = options.HANDS

    def sonification(self):
        self.set_status(STATUS.PLAYING)
        print("ready to sonification!")
        hand = HandFeature(image_points=average_points(self.hand_frames))
        send_to_max(hand)
        sound_duration = 10
        print("time taken {}".format(time.time() - self.start_time))

        store(
            data_class="OneHandFeatures",
            data=dict(
                uid=hand.uid,
                touch_session_id=self.session_id,
                image_points=hand.image_points
            )
        )
        for picture in self.hand_frames:
            picture.save()

        time.sleep(sound_duration)
        self.reset()

    def reset(self):
        self.session_id = None
        self.hand_frames = []
        self.set_status(STATUS.IDLE)
        self.start_time = None

    def process_message(self, body, message):
        super().process_message(body, message)
        now = datetime.now()
        touch = load(body.get("pk"), data_class=self.data_class)
        delta = now - touch.create_time
        if delta.seconds > 1:
            print("skip frame")
            return
        if self.session_id is None or touch.session_id != self.session_id or not touch.status:
            self.reset()
        print("{} - {}".format(touch.session_id, touch.status))
        if touch.status:
            if self.status in [STATUS.COMPUTING, STATUS.IDLE]:
                self.set_status(STATUS.COMPUTING)
                self.session_id = touch.session_id
                self.process_frame(self.video_source, self.session_id)
        # self.refresh_hand_frames(self.session_id)
        if len(self.hand_frames) >= self.hands_to_sonification:
            self.sonification()

    def refresh_hand_frames(self, session_id):
        self.hand_frames = find(self.hand_data_class, dict(session_id=session_id))

    def process_frame(self, video_source, session_id):
        frame = VideoGrabber(video_source).grab()
        extractor = HandFeatureExtractor(live_output=False)
        image_points, output_frame = extractor.process_frame(frame)
        if self.session_id != session_id or self.status == STATUS.PLAYING:
            print("im late!")
            return
        if image_points is not None:
            if self.start_time is None:
                self.start_time = time.time()
            filename = temporary_name() + settings.ONEHAND_HAND_PICTURES_EXTENSION
            filepath = os.path.join(settings.ONEHAND_HAND_PICTURES_FOLDER,
                                    filename) + settings.ONEHAND_HAND_PICTURES_EXTENSION
            cv2.imwrite(filepath, frame)
            # DEBUG
            processed_filepath = os.path.join(settings.ONEHAND_HAND_PICTURES_FOLDER,
                                              filename) + "processed" + settings.ONEHAND_HAND_PICTURES_EXTENSION
            cv2.imwrite(processed_filepath, output_frame)
            print("hand detected!")
            self.hand_frames.append(
                create(data_class="OneHandPicture",
                       data=dict(
                           touch_session_id=session_id,
                           hand=True,
                           src=filepath,
                           filename=filename,
                           image_points=image_points,
                       )
                       )
            )
        else:
            # save no hands images?
            print("no hands!")


if __name__ == "__main__":
    service = DuBio()
    service.run()
