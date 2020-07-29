import RPi.GPIO as GPIO
from ._buzzer_gpio_config import BuzzerGpioConfig

buzzer_name_a = "a"
buzzer_name_b = "b"


class BuzzerCore:

    _lock = False

    def __init__(self, gpio_config: BuzzerGpioConfig):
        self._gpio_config = gpio_config

    def register_buzzer_callback(self, buzzer_callback: BuzzerCallback):
        self.buzzer_callbacks.add(buzzer_callback)

    def unregister_buzzer_callback(self, buzzer_callback: BuzzerCallback):
        self.buzzer_callbacks.remove(buzzer_callback)

    def _setup(self):
        GPIO.setup(self._gpio_config.get_pin_a(), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self._gpio_config.get_pin_b(), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(self._gpio_config.get_pin_a(), GPIO.RISING, callback=self._callback_a)
        GPIO.add_event_detect(self._gpio_config.get_pin_b(), GPIO.RISING, callback=self._callback_b)

    def _callback_a(self):
        pass

    def _callback_b(self):
        pass
