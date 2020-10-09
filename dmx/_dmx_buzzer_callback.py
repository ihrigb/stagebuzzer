import buzzer
import config
from ._dmx_output import DmxOutput


class DmxBuzzerCallback(buzzer.BuzzerCallback):

    def __init__(self, output: DmxOutput, dmx_config: config.DmxConfig):
        self._output = output
        self._dmx_config = dmx_config

    def on_buzz(self, buz: buzzer.Buzzer):
        address = self._dmx_config.get_dmx_address(buz.get_name())
        value = self._dmx_config.get_dmx_value(buz.get_name())
        self._output.set(address, value)

    def reset(self):
        self._output.reset()
