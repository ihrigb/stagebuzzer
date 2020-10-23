import serial
import sys

DMXOPEN = bytes([126])
DMXCLOSE = bytes([231])
DMXINTENSITY = bytes([6]) + bytes([1]) + bytes([2])
DMXINIT1 = bytes([3]) + bytes([2]) + bytes([0]) + bytes([0]) + bytes([0])
DMXINIT2 = bytes([10]) + bytes([2]) + bytes([0]) + bytes([0]) + bytes([0])


class Dmx:
    def __init__(self, serial_port='/dev/ttyUSB0'):
        try:
            self._serial = serial.Serial(serial_port, baudrate=57600)
        except:
            print("Error: could not open Serial Port")
            sys.exit(1)
        self._serial.write(DMXOPEN + DMXINIT1 + DMXCLOSE)
        self._serial.write(DMXOPEN + DMXINIT2 + DMXCLOSE)

        self._dmx_data = [bytes([0])] * 513  # 512 plus "space".

    def set_channel(self, channel: int, value: int):
        if channel > 512:
            channel = 512
        if channel < 0:
            channel = 0
        if value > 255:
            value = 255
        if value < 0:
            value = 0
        self._dmx_data[channel - 1] = bytes([value])

    def blackout(self):
        for i in range(1, 512, 1):
            self.set_channel(i, 0)

    def render(self):
        sdata = b''.join(self._dmx_data)
        self._serial.write(DMXOPEN + DMXINTENSITY + sdata + DMXCLOSE)
