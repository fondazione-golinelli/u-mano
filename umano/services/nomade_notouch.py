import asyncio
import json
import websockets


from umano.hal.db import database
messages = database.onehand.messages

UI = set()


def state_event():
    return json.dumps({"state": "IDLE", "value": "ok"})


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


async def consume_message():
    global messages
    message = None
    while message is None:
        message = messages.find_one()
        await asyncio.sleep(0.1)
    print("Found message! {} - {}".format(message.get("state"), message.get("value")))
    messages.delete_one({"_id": message.get("_id")})
    return json.dumps({"state": message.get("state"), "value": message.get("value")})


async def websocket_handler(websocket, path):
    await register(websocket)
    while True:
        message = await consume_message()
        await websocket.send(message)


if __name__ == "__main__":

    start_server = websockets.serve(websocket_handler, "0.0.0.0", 6789, ping_interval=None)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()