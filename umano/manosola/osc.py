import time
from pythonosc.udp_client import SimpleUDPClient

from umano.manosola import settings

osc_client = SimpleUDPClient(address=settings.MAX_HOST, port=settings.MAX_PORT)


def send_to_max(hand, all=True, only_durer=False, only_hand=False):
    if all:
        osc_client.send_message(settings.OSC_DURER_FREQ_ADDRESS, hand.durer_frequencies)
        osc_client.send_message(settings.OSC_DURER_AMP_ADDRESS, hand.durer_amplitudes)
        osc_client.send_message(settings.OSC_HAND_FREQ_ADDRESS, hand.frequencies)
        osc_client.send_message(settings.OSC_HAND_AMP_ADDRESS, hand.amplitudes)

    elif only_durer:
        osc_client.send_message(settings.OSC_DURER_FREQ_ADDRESS, hand.durer_frequencies)
        osc_client.send_message(settings.OSC_DURER_AMP_ADDRESS, hand.durer_amplitudes)
        osc_client.send_message(settings.OSC_HAND_FREQ_ADDRESS, hand.zeros)
        osc_client.send_message(settings.OSC_HAND_AMP_ADDRESS, hand.ones)

    elif only_hand:
        osc_client.send_message(settings.OSC_DURER_FREQ_ADDRESS, hand.zeros)
        osc_client.send_message(settings.OSC_DURER_AMP_ADDRESS, hand.ones)
        osc_client.send_message(settings.OSC_HAND_FREQ_ADDRESS, hand.frequencies)
        osc_client.send_message(settings.OSC_HAND_AMP_ADDRESS, hand.amplitudes)

    time.sleep(1)
    osc_client.send_message(settings.OSC_BIGBANG_ADDRESS, ["bang"])
