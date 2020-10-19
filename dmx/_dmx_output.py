from ._dmx import Dmx


class DmxOutput:

    def __init__(self):
        self._dmx = Dmx('/dev/ttyUSB0')
        self._dmx.blackout()
        self._dmx.render()

    def set(self, channel: int, value: int):
        self._dmx.set_channel(channel, value)

    def reset(self, channel: int):
        self.set(channel, 0)

    def reset(self):
        self._dmx.blackout()

    def flush(self):
        self._dmx.render()
