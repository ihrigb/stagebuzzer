import config
import buzzer
import logging


class AudioCallback(buzzer.BuzzerCallback):
    def __init__(self, audio_config: config.AudioConfig):
        self._audio_config = audio_config

    def on_buzz(self, buz: str):
        logging.debug('Audio callback called.')
        if not self._audio_config.get_active():
            logging.debug('Audio callback is not active.')
            return
        pass

    def reset(self):
        logging.debug('Audio callback reset.')
        pass
