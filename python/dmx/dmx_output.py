dmx_channels = 512


class DmxOutput:

    channels = dict

    def set(self, channel: int, value: int):
        self.channels[channel] = value

    def reset(self, channel: int):
        self.set(channel, 0)

    def reset(self):
        for channel in range(dmx_channels):
            self.reset(channel)

    def flush(self):
        pass
