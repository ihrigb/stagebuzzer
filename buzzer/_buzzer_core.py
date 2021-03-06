import RPi.GPIO as GPIO
import time
import logging
import threading
import config
from ._buzzer_gpio_config import BuzzerGpioConfig
from ._buzzer_callback import BuzzerCallback

buzzer_name_a = "1"
buzzer_name_b = "2"

_gpio = BuzzerGpioConfig(2, 3)


class BuzzerCore:

    _lock = False
    _active_buzzer = None

    def __init__(self, general_config: config.GeneralConfig, buzzer_callbacks: list):
        self._general_config = general_config
        self._buzzer_callbacks = buzzer_callbacks

        GPIO.setup(_gpio.get_pin_1(), GPIO.IN)
        GPIO.setup(_gpio.get_pin_2(), GPIO.IN)

        GPIO.add_event_detect(_gpio.get_pin_1(), GPIO.FALLING, callback=self._callback_1)
        GPIO.add_event_detect(_gpio.get_pin_2(), GPIO.FALLING, callback=self._callback_2)

    def register_buzzer_callback(self, buzzer_callback: BuzzerCallback):
        self._buzzer_callbacks.append(buzzer_callback)

    def unregister_buzzer_callback(self, buzzer_callback: BuzzerCallback):
        self._buzzer_callbacks.remove(buzzer_callback)

    def _callback_1(self, channel):
        time.sleep(0.01)
        if GPIO.input(_gpio.get_pin_1()):  # keep in mind this is pulled up
            return
        self._callback('1')

    def _callback_2(self, channel):
        time.sleep(0.01)
        if GPIO.input(_gpio.get_pin_2()):  # keep in mind this is pulled up
            return
        self._callback('2')

    def _reset(self):
        logging.debug('Waiting for hold time to expire ({} s).'.format(self._general_config.get_hold_time()))
        time.sleep(self._general_config.get_hold_time())

        logging.info('Hold time expired. Resetting...')

        for callback in self._buzzer_callbacks:
            threading.Thread(target=callback.reset).start()

        self._lock = False
        self._active_buzzer = None

    def _callback(self, buz: str):
        logging.info('Buzzer {} pressed.'.format(buz))
        if self._lock:
            logging.info('Buzzer already locked by {}'.format(self._active_buzzer))
            return

        logging.debug('Setting lock for buzzer {}.'.format(buz))

        self._lock = True
        self._active_buzzer = buz

        for callback in self._buzzer_callbacks:
            callback.on_buzz(buz)

        threading.Thread(target=self._reset).start()
