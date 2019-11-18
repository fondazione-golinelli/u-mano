
from serial.tools.miniterm import Miniterm

from umano import settings
from umano.adam.models import emg_sensors_serial, OSCConsole

if __name__ == "__main__":
    ser = emg_sensors_serial()
    ser.open()
    terminal = Miniterm(ser)
    terminal.console = OSCConsole(host=settings.ADAM_OSC_RECEIVER_HOST, port=settings.ADAM_OSC_RECEIVER_PORT,
                                  address=settings.ADAM_OSC_PRESSURE_ADDRESS)
    terminal.set_rx_encoding(settings.ADAM_SERIAL_ENCODING)
    terminal.start()
