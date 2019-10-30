from optparse import make_option

from umano.services.base import UmanoStreamService
from umano.tools.camera_stream.app import main, AVAILABLE_PROCESSORS


class CameraStreamService(UmanoStreamService):
    help = "Stream a camera capture trough http"
    option_list = UmanoStreamService.option_list + [
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
        )
    ]

    def execute(self, *args, **options):
        parser = self.create_parser()
        options, args = parser.parse_args()
        main(options)


if __name__ == "__main__":
    service = CameraStreamService()
    service.run()
