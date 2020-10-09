import buzzer
import config
from ._dmx_output import DmxOutput


class DmxBuzzerCallback(buzzer.BuzzerCallback):

    def __init__(self, output: DmxOutput, dmx_config: config.DmxConfig):
        self._output = output
        self._dmx_config = dmx_config

    def on_buzz(self, buz: str):
        address = self._dmx_config.get_dmx_address(buz)
        value = self._dmx_config.get_dmx_value(buz)
        self._output.set(address, value)

    def reset(self):
        self._output.reset()
