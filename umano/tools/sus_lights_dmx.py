import sys
from pythonosc import udp_client

from umano import settings

client = udp_client.SimpleUDPClient(settings.SUS_MILLUMIN_HOST, settings.SUS_MILLUMIN_PORT)

if __name__ == "__main__":
    value = float(sys.argv[1])
    client.send_message(settings.SUS_OSC_MASTERS_DMX_ADDRESS, value)
    sys.exit(0)
