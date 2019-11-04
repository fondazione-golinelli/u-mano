import os
import string
import cv2
from umano.tools.camera_stream.base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = 0
    processor = None
    file_extension = None

    def __init__(self, source=0, processor=None, file_extension=".png"):
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
    def set_file_extension(file_extension):
        Camera.file_extension = file_extension

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source, cv2.CAP_DSHOW)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera {}'.format(Camera.video_source))

        while True:
            # read current frame
            _, img = camera.read()

            if Camera.processor is not None:
                img = Camera.processor.process_frame(img)

            # encode as a jpeg image and return it
            yield cv2.imencode(Camera.file_extension, img)[1].tobytes()
