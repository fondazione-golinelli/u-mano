import sys
from pythonosc import udp_client

host = "localhost"
port = 9999

client = udp_client.SimpleUDPClient(host, port)

if __name__ == "__main__":
    if sys.argv[1] == '1':
        client.send_message("/umano/live/playing/start", 1)
    elif sys.argv[1] == '0':
        client.send_message("/umano/live/playing/stop", 1)
    else:
        print("argument not recognized")
    sys.exit(0)
