import argparse
import string
from flask import Flask, render_template, Response
from camera_opencv import Camera
import image_processing

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html', title=app.config.get("title"))


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        l = str(len(frame)).encode("utf-8")
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\nContent-Length: ' + l + b'\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera(app.config.get("camera_source"), processor=extra_config['processor'])),
                    mimetype='multipart/x-mixed-replace; boundary=--frame')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--port',
        dest='port',
        type=int,
        default=5000,
        help='port to listen to (default 5000)')
    parser.add_argument(
        '-t',
        '--title',
        dest='title',
        type=str,
        default="Camera",
        help='default title for web page (default Camera)')
    parser.add_argument(
        '-c',
        '--camera',
        dest='camera',
        type=str,
        default="0",
        help='local camera index to stream from (default 0)')

    AVAILABLE_PROCESSORS = ["BaseProcessing","BackgroundSubtraction"]

    parser.add_argument(
        '--processor',
        dest='processor',
        type=str,
        default="BaseProcessing",
        help='image processing to apply to frame {}'.format(AVAILABLE_PROCESSORS))

    parser.print_help()

    args = parser.parse_args()

    extra_config = dict(title=args.title)

    if args.camera in string.digits:
        extra_config['camera_source'] = int(args.camera)
    else:
        extra_config['camera_source'] = args.camera

    if args.processor not in AVAILABLE_PROCESSORS:
        raise RuntimeError("Processor {} not available".format(args.processor))

    extra_config['processor'] = getattr(image_processing, args.processor)()

    app.config.update(extra_config)

    app.run(host='0.0.0.0', port=args.port, threaded=True)
