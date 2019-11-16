import os
import random
import time
from pythonosc.udp_client import SimpleUDPClient

from umano.onehand.models import Bjorklund
from umano import settings


def send_sonification_to_max(hand, all=True, only_durer=False, only_hand=False, host=settings.ONEHAND_MAX_HOST,
                             port=settings.ONEHAND_MAX_PORT):
    osc_client = SimpleUDPClient(address=host, port=port)

    if all:
        osc_client.send_message(settings.ONEHAND_OSC_DURER_FREQ_ADDRESS, hand.durer_frequencies)
        osc_client.send_message(settings.ONEHAND_OSC_DURER_AMP_ADDRESS, hand.durer_amplitudes)
        osc_client.send_message(settings.ONEHAND_OSC_HAND_FREQ_ADDRESS, hand.frequencies)
        osc_client.send_message(settings.ONEHAND_OSC_HAND_AMP_ADDRESS, hand.amplitudes)

    elif only_durer:
        osc_client.send_message(settings.ONEHAND_OSC_DURER_FREQ_ADDRESS, hand.durer_frequencies)
        osc_client.send_message(settings.ONEHAND_OSC_DURER_AMP_ADDRESS, hand.durer_amplitudes)
        osc_client.send_message(settings.ONEHAND_OSC_HAND_FREQ_ADDRESS, hand.zeros)
        osc_client.send_message(settings.ONEHAND_OSC_HAND_AMP_ADDRESS, hand.ones)

    elif only_hand:
        osc_client.send_message(settings.ONEHAND_OSC_DURER_FREQ_ADDRESS, hand.zeros)
        osc_client.send_message(settings.ONEHAND_OSC_DURER_AMP_ADDRESS, hand.ones)
        osc_client.send_message(settings.ONEHAND_OSC_HAND_FREQ_ADDRESS, hand.frequencies)
        osc_client.send_message(settings.ONEHAND_OSC_HAND_AMP_ADDRESS, hand.amplitudes)

    osc_client.send_message(settings.ONEHAND_OSC_HAND_BEAT_ADDRESS, hand.beats)
    osc_client.send_message(settings.ONEHAND_OSC_HAND_ENVELOPE_ADDRESS, hand.envelopes)

    file_path = os.path.normpath(os.path.join(
        settings.ONEHAND_HAND_AUDIO_FOLDER,
        "{}{}".format(hand.uid, settings.ONEHAND_HAND_AUDIO_EXTENSION)
    )).replace("\\", "/")
    osc_client.send_message(settings.ONEHAND_OSC_RECORD_FILENAME_ADDRESS, [file_path])

    time.sleep(1)
    osc_client.send_message(settings.ONEHAND_OSC_BANG_ADDRESS, ["bang"])
    hand.metronome.reset()
    idf = 0
    while hand.metronome.has_next():

        if hand.metronome.counter % hand.metronome.beat_resolution == 0 \
                and hand.drum_pattern[hand.metronome.counter // hand.metronome.beat_resolution] or random.randint(0, 100) > 80:
            osc_client.send_message(settings.ONEHAND_OSC_HAND_BEAT_BANG_ADDRESS,
                                    [1, hand.frequencies[idf]])
            idf = (idf + 1) % len(hand.frequencies)
        time.sleep(hand.metronome.time_division)
        hand.metronome.tick()


def send_to_vuo(hand, host=settings.ONEHAND_VUO_HOST, port=settings.ONEHAND_VUO_PORT):
    osc_client = SimpleUDPClient(address=host, port=port)
    for finger, i, data in hand.finger_to_finger():
        osc_client.send_message(settings.ONEHAND_OSC_FINGER_ADDRESS.format(finger, i), data)


def send_cave_to_vuo(hands, host=settings.ONEHAND_VUO_HOST, port=settings.ONEHAND_VUO_PORT):
    osc_client = SimpleUDPClient(address=host, port=port)

    osc_client.send_message("/umano/onehand/cave/hands/join",
                            [";".join(map(str, [hand.uid, hand.position.x, hand.position.y, hand.size.w, hand.size.h,
                                                hand.rotation]))
                             for hand in hands])
    # osc_client.send_message("/umano/onehand/cave/hands/testlist", [[hand.uid, hand.uid, hand.uid] for hand in hands])
    # osc_client.send_message("/umano/onehand/cave/hands/totem", [hand.uid for hand in hands])
    # osc_client.send_message("/umano/onehand/cave/hands/features", [hand.features_image for hand in hands])
    # osc_client.send_message("/umano/onehand/cave/hands/position/x", [hand.position.x for hand in hands])
    # osc_client.send_message("/umano/onehand/cave/hands/position/y", [hand.position.y for hand in hands])
    # osc_client.send_message("/umano/onehand/cave/hands/size/width", [hand.size.w for hand in hands])
    # osc_client.send_message("/umano/onehand/cave/hands/size/height", [hand.size.h for hand in hands])
