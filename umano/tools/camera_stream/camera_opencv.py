import os
import string
import cv2
from umano.tools.camera_stream.base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = 0
    processor = None
    file_extension = None
    capture = None

    def __init__(self, source=0, processor=None, file_extension=".jpeg", capture=None):
        if capture is not None:
            Camera.set_capture(capture)
        else:
            Camera.set_video_source(source)
        Camera.set_camera_processor(processor)
        Camera.set_file_extension(file_extension)
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
    def set_capture(capture):
        Camera.capture = capture

    @staticmethod
    def set_file_extension(file_extension):
        Camera.file_extension = file_extension

    @staticmethod
    def frames():
        if Camera.capture is not None:
            camera = Camera.capture
        else:
            camera = cv2.VideoCapture(Camera.video_source, cv2.CAP_DSHOW)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera {}'.format(Camera.video_source))

        while True:
            # read current frame
            _, frame = camera.read()

            from umano.onehand.utils import rescale_frame
            frame = rescale_frame(frame, wpercent=50, hpercent=50)

            if Camera.processor is not None:
                frame = Camera.processor.process_frame(frame)

            # encode as a jpeg image and return it
            flag, encoded_image = cv2.imencode(Camera.file_extension, frame)
            # yield cv2.imencode(Camera.file_extension, img)[1].tobytes()
            yield bytearray(encoded_image)
