import config
import buzzer
import logging
import simpleaudio


class AudioCallback(buzzer.BuzzerCallback):
    _play_object = None

    def __init__(self, audio_config: config.AudioConfig):
        self._audio_config = audio_config
        self._wave_object = simpleaudio.WaveObject.from_wave_file('/mnt/usb/AirHorn.wav')

    def on_buzz(self, buz: str):
        logging.debug('Audio callback called.')
        if not self._audio_config.get_active():
            logging.debug('Audio callback is not active.')
            return

        if self._play_object is not None:
            logging.error('Already playing sound.')
            return

        self._play_object = self._wave_object.play()

    def reset(self):
        logging.debug('Audio callback reset.')

        if self._play_object is not None:
            self._play_object.stop()
        self._play_object = None
