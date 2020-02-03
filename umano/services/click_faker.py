from datetime import datetime
import sys
import time
import uuid

from umano.hal.data import store


def new_touch_session_id():
    return str(uuid.uuid4())


def trigger_touch_event(session_id, status):
    print("Touch {} {}".format(session_id, status))
    store(data_class="OneHandTouch", data=dict(session_id=session_id, status=status))


if __name__ == "__main__":
    print("hello faker")
    while True:
        if 6 < datetime.now().hour < 22:
            try:
                time.sleep(2)
                session_id = new_touch_session_id()
                trigger_touch_event(session_id, True)
                time.sleep(5)
                trigger_touch_event(session_id, False)
            except KeyboardInterrupt:
                sys.exit(0)
