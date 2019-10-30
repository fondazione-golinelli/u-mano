import argparse
import pyclbr

from flask import Flask, render_template, Response

from umano.tools.camera_stream.camera_opencv import Camera
from umano.tools.camera_stream import image_processing

app = Flask(__name__)

AVAILABLE_PROCESSORS = [k for k, v in pyclbr.readmodule("umano.tools.camera_stream.image_processing").items() if
                        isinstance(v, pyclbr.Class)]


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html', title=app.config.get("TITLE"))


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
    return Response(
        gen(Camera(app.config.get("CAMERA_SOURCE"), processor=app.config.get('IMAGE_PROCESSOR', "BaseProcessing"))),
        mimetype='multipart/x-mixed-replace; boundary=--frame')


def main(config):
    if not isinstance(config, dict):
        app.config.update(config.__dict__)
    else:
        app.config.update(config)

    if app.config.get("IMAGE_PROCESSOR") not in AVAILABLE_PROCESSORS:
        raise RuntimeError("Processor {} not available".format(app.config.get("IMAGE_PROCESSOR")))

    app.config['IMAGE_PROCESSOR'] = getattr(image_processing, app.config.get("IMAGE_PROCESSOR"))()

    app.run(app.config.get("HOST", "0.0.0.0"), port=app.config.get("PORT", 5000), threaded=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--port',
        dest='PORT',
        type=int,
        default=5000,
        help='port to listen to (default 5000)')
    parser.add_argument(
        '-t',
        '--title',
        dest='TITLE',
        type=str,
        default="Camera",
        help='default title for web page (default Camera)')
    parser.add_argument(
        '-c',
        '--camera',
        dest='CAMERA_SOURCE',
        type=str,
        default="0",
        help='local camera index to stream from (default 0) or camera stream url')
    parser.add_argument(
        '--processor',
        dest='IMAGE_PROCESSOR',
        type=str,
        default="BaseProcessing",
        help='image processing to apply to frame {}'.format(AVAILABLE_PROCESSORS))

    args = parser.parse_args()

    main(args)
