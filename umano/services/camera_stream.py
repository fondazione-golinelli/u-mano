from optparse import make_option

from umano.hal.data import store
from umano.services.base import UmanoServerService, STATUS
from umano.tools.camera_stream.app import create_app, AVAILABLE_PROCESSORS

from umano import settings


class CameraStreamService(UmanoServerService):
    help = "Stream a camera capture trough http"
    option_list = UmanoServerService.option_list + [
        make_option(
            '-t',
            '--title',
            dest='TITLE',
            type=str,
            default="Camera",
            help='default title for web page (default Camera)'
        ),
        make_option(
            '-c',
            '--camera',
            dest='CAMERA_SOURCE',
            type=str,
            default="0",
            help='local camera index to stream from (default 0) or camera stream url'
        ),
        make_option(
            '--processor',
            dest='IMAGE_PROCESSOR',
            type=str,
            default="BaseProcessing",
            help='image processing to apply to frame {}'.format(AVAILABLE_PROCESSORS)
        ),
        make_option(
            '--file-extension',
            dest='FILE_EXTENSION',
            type=str,
            default=".png",
            help='image file type to output (default ".png")'
        )
    ]

    def __init__(self, capture=None) -> None:
        super().__init__()
        self.streaming_document = None
        self.url = None
        self.capture = capture

    def register(self):
        self.streaming_document = store(
            data_class="ServiceStreamingData",
            data=dict(
                host=self.host,
                ip=self.ip,
                name=self.name,
                url=self.url,
                description=self.description
            )
        )

    def unregister(self):
        self.streaming_document.delete()

    def execute(self, args, options):
        self.set_status(STATUS.STREAMING)
        app = create_app(options)
        app.service = self
        app.capture = capture
        self.url = "http://{}:{}{}".format(self.ip, app.config.get("PORT", 5000), settings.CAMERA_STREAM_LIVE_URL)
        self.register()
        app.run(app.config.get("HOST", "0.0.0.0"), port=app.config.get("PORT", 5000), threaded=True)
        self.unregister()
        raise KeyboardInterrupt


if __name__ == "__main__":
    import cv2
    capture = cv2.VideoCapture(0)
    service = CameraStreamService(capture=capture)
    service.run()
