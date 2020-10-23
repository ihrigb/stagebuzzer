from ._open_dmx_usb import OpenDmxUsb


class DmxOutput:

    def __init__(self):
        super().__init__()
        self._dmx = OpenDmxUsb()
        self._dmx.start()
        self._channels = [0] * 513

    def set(self, channel: int, value: int):
        self._channels[channel] = value

    def reset(self, channel: int):
        self.set(channel, 0)

    def reset(self):
        self._channels = [0] * 513

    def flush(self):
        self._dmx.set_channel_values(self._channels)
