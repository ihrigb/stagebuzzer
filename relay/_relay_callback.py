import config
from buzzer import BuzzerCallback
from._relay_output import RelayOutput


class RelayCallback(BuzzerCallback):
    def __init__(self, output: RelayOutput, config: config.RelayConfig):
        self._relay_output = output
        self._config = config

    def on_buzz(self, buzzer: str):
        if (self._config.get_active()):
            self._relay_output.enable_relay(buzzer)

    def reset(self):
        self._relay_output.reset()
