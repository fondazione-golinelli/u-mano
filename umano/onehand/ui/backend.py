from enum import auto, IntEnum
import asyncio
import json
import logging
import websockets
import cv2

from umano.onehand.handfeatures.extractor import HandFeatureExtractor
from umano.onehand.osc import send_to_max

extractor = HandFeatureExtractor(live_output=True)


class VideoGrabber(object):

    def __init__(self, video_source=None):
        self.video_source = video_source

    def grab(self):
        capture = cv2.VideoCapture(self.video_source)
        if capture.isOpened():
            _, frame = capture.read()
            capture.release()
            return frame
        return None


VIDEO_SOURCE = "http://127.0.0.1:5000/video_feed"

logging.basicConfig()


class Status(IntEnum):
    IDLE = auto()
    TOUCHING = auto()
    ACQUIRING = auto()
    COMPUTING = auto()
    PLAYING = auto()


STATE = Status.IDLE

UI = set()


def state_event():
    return json.dumps({"type": "state", "value": str(STATE)})


def ui_event():
    return json.dumps({"type": "ui", "count": len(UI)})


async def notify_state():
    if UI:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([ui.send(message) for ui in UI])


async def register(websocket):
    UI.add(websocket)
    await notify_state()


async def unregister(websocket):
    UI.remove(websocket)
    await notify_state()


async def acquire_image():
    hand = None
    while hand is None:
        frame = VideoGrabber(VIDEO_SOURCE).grab()
        if frame is None:
            break
        hand, processed_frame = extractor.process_frame(frame)


async def onehand_backend(websocket, path):
    global STATE
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "touch_start":
                STATE = Status.TOUCHING
                await notify_state()
            elif data["action"] == "touch_end":
                if STATE in [Status.TOUCHING, Status.IDLE]:
                    STATE = Status.IDLE

                await notify_state()

            elif data['action'] == "hand_on":
                STATE = Status.ACQUIRING
                await acquire_image()

            elif data['action'] == "hand_off":
                if STATE == Status.ACQUIRING:
                    STATE = Status.IDLE

            else:
                logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)


start_server = websockets.serve(onehand_backend, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
