from pythonosc.udp_client import SimpleUDPClient

import serial
from serial.tools.miniterm import Console
from umano import settings


def pressure_sensors_serial():
    ser = serial.Serial()
    ser.port = settings.ADAM_SERIAL_PRESSURE_PORT
    ser.baudrate = settings.ADAM_SERIAL_BAUDRATE
    return ser


def emg_sensors_serial():
    ser = serial.Serial()
    ser.port = settings.ADAM_SERIAL_EGM_PORT
    ser.baudrate = settings.ADAM_SERIAL_BAUDRATE
    return ser


class OSCConsole(Console):

    def __init__(self, host, port, address):
        self.client = SimpleUDPClient(address=host, port=port)
        self.address = address
        self.line = ""

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
