import os
import string
import cv2
from umano.tools.camera_stream.base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = 0
    processor = None

    def __init__(self, source=0, processor=None):
        Camera.set_video_source(source)
        Camera.set_camera_processor(processor)
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        if source in string.digits:
            source = int(source)
        Camera.video_source = source

    @staticmethod
    def set_camera_processor(processor):
        Camera.processor = processor

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera {}'.format(Camera.video_source))

        while True:
            # read current frame
            _, img = camera.read()

            if Camera.processor is not None:
                img = Camera.processor.process_frame(img)

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
