from enum import auto, IntEnum
import asyncio
import json
import logging
import websockets
import uuid

from umano.hal.data import store
from umano.services.base import UmanoServerService, STATUS

logging.basicConfig()


STATE = STATUS.IDLE
TOUCH_ID = None
UI = set()


def state_event():
    return json.dumps({"type": "state", "value": STATE.name})


def ui_event():
    return json.dumps({"type": "ui", "count": len(UI)})


async def notify_state():
    if UI:
        message = state_event()
        await asyncio.wait([ui.send(message) for ui in UI])


async def register(websocket):
    UI.add(websocket)
    await notify_state()


async def unregister(websocket):
    UI.remove(websocket)
    await notify_state()


async def hand_on_callback(session_id, status):
    store(data_class="OneHandTouch", data=dict(session_id=session_id, status=status))
    print("Touch {} {}".format(session_id, status))


async def onehand_backend(websocket, path):
    global STATE
    global TOUCH_ID
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "touch_start":
                STATE = STATUS.TOUCHING

            elif data["action"] == "touch_end":
                if STATE in [STATUS.TOUCHING, STATUS.IDLE]:
                    STATE = STATUS.IDLE

            elif data['action'] == "hand_on":
                STATE = STATUS.ACQUIRING

                if TOUCH_ID is None:
                    TOUCH_ID = str(uuid.uuid4())
                await hand_on_callback(TOUCH_ID, True)

            elif data['action'] == "hand_off":
                if STATE == STATUS.ACQUIRING:
                    STATE = STATUS.IDLE
                    await hand_on_callback(TOUCH_ID, False)
                    TOUCH_ID = None
            else:
                logging.error("unsupported event: {}", data)

            await notify_state()
    finally:
        await unregister(websocket)


class NoMade(UmanoServerService):

    def __init__(self) -> None:
        super().__init__()
        self.name = "NoMade"
        self.description = "Control the OneHand interface via websocket"

    def execute(self, args, options):
        start_server = websockets.serve(onehand_backend, options.HOST, options.PORT)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
        self.terminate()


if __name__ == "__main__":
    service = NoMade()
    service.run()
