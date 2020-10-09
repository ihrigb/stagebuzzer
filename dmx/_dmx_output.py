from ._dmx import Dmx

dmx_channels = 512


class DmxOutput:

    _dmx = Dmx('/dev/ttyUSB0')

    def set(self, channel: int, value: int):
        self._dmx.set_channel(channel, value)

    def reset(self, channel: int):
        self.set(channel, 0)

    def reset(self):
        self._dmx.blackout()

    def flush(self):
        self._dmx.render()
