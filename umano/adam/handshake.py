from pythonosc.udp_client import SimpleUDPClient

import serial
from serial.tools.miniterm import Miniterm, Console

from umano import settings
from umano.onehand.durer import durerizer
from umano.onehand.utils import points_to_frequencies


def pressure_sensors_serial():
    ser = serial.Serial()
    ser.port = settings.ADAM_SERIAL_PRESSURE_PORT
    ser.baudrate = settings.ADAM_SERIAL_BAUDRATE
    return ser


class OSCConsole(Console):

    def __init__(self, host, port, address):
        self.client = SimpleUDPClient(address=host, port=port)
        self.address = address
        self.line = ""
        self.durer_frequencies, self.durer_distances, _ = points_to_frequencies(durerizer(1024), 64)
        self.client.send_message(settings.ONEHAND_OSC_DURER_FREQ_ADDRESS, self.durer_frequencies)

    def write(self, text):
        self.line += text
        if "\r\n" in self.line:
            self.line = self.line.replace("\r\n", "")
            print(self.line)
            self.osc_send(self.line)
            self.line = ""

    def osc_send(self, text):
        data = list(map(float, text.split("\t")))
        self.client.send_message(self.address, data)


if __name__ == "__main__":
    ser = pressure_sensors_serial()
    ser.open()
    terminal = Miniterm(ser)
    terminal.console = OSCConsole(host=settings.ADAM_OSC_RECEIVER_HOST, port=settings.ADAM_OSC_RECEIVER_PORT,
                                  address=settings.ADAM_OSC_PRESSURE_ADDRESS)
    terminal.set_rx_encoding(settings.ADAM_SERIAL_ENCODING)
    terminal.start()
    # ser.open()
    # while True:
    #     try:
    #         data = ser.readline()
    #         text = decoder.decode(data)
    #         print(text)
    #     except KeyboardInterrupt:
    #         sys.exit(0)
