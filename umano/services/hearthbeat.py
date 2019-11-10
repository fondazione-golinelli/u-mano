import random
import sys
import time
from pythonosc.udp_client import SimpleUDPClient

from umano import settings


client = SimpleUDPClient(settings.ONEHAND_MILLUMIN_HOST, settings.ONEHAND_MILLUMIN_PORT)

repetitions = [
    3.0,
    5.0,
    15.0,

]

while True:
    try:

        time.sleep(10)

        for x in range(10):
            seed = round(random.random(),2)
            client.send_message(settings.ONEHAND_OSC_RANDOM_SEED_ADDRESS, seed)
            print("sent seed {}".format(seed))
            time.sleep(0.5 * random.random())
            if random.randint(0, 100) > 50:
                repetition = round(random.random() * 12.0 + 3.0, 2)
                client.send_message(settings.ONEHAND_OSC_RANDOM_REPETITION_ADDRESS, repetition)
                print("sent repetition {}".format(repetition))

        if random.randint(0, 100) > 67:
            client.send_message(settings.ONEHAND_OSC_RANDOM_ENABLE_ADDRESS, 0)
            print("sent enable false")
            time.sleep(21)
            client.send_message(settings.ONEHAND_OSC_RANDOM_ENABLE_ADDRESS, 1)
            print("sent enable enable")


    except KeyboardInterrupt:
         sys.exit(0)

