import os
import time
from pythonosc.udp_client import SimpleUDPClient

from umano import settings


def send_to_max(hand, all=True, only_durer=False, only_hand=False, host=settings.ONEHAND_MAX_HOST,
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
    osc_client.send_message(settings.ONEHAND_OSC_HAND_ATTACK_ADDRESS, hand.attacks)
    osc_client.send_message(settings.ONEHAND_OSC_HAND_RELEASE_ADDRESS, hand.releases)

    file_path = os.path.normpath(os.path.join(
        settings.ONEHAND_HAND_AUDIO_FOLDER,
        "{}{}".format(hand.uid, settings.ONEHAND_HAND_AUDIO_EXTENSION)
    )).replace("\\", "/")
    osc_client.send_message(settings.ONEHAND_OSC_RECORD_FILENAME_ADDRESS, [file_path])

    time.sleep(1)
    osc_client.send_message(settings.ONEHAND_OSC_BANG_ADDRESS, ["bang"])


def send_to_vuo(hand, host=settings.ONEHAND_VUO_HOST, port=settings.ONEHAND_VUO_PORT):
    osc_client = SimpleUDPClient(address=host, port=port)
    for finger, i, data in hand.finger_to_finger():
        osc_client.send_message(settings.ONEHAND_OSC_FINGER_ADDRESS.format(finger, i), data)
