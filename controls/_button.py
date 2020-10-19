import time
import RPi.GPIO as GPIO
from typing import Callable

_output_dict = {True: GPIO.HIGH, False: GPIO.LOW}


class Button:
    def __init__(self, name: str, gpio_btn_pin: int, gpio_led_pin: int, on_push: Callable[[int], None]):
        self._name = name
        self._gpio_btn_pin = gpio_btn_pin
        self._gpio_led_pin = gpio_led_pin
        self._on_push = on_push

        GPIO.setup(gpio_btn_pin, GPIO.IN)
        GPIO.setup(gpio_led_pin, GPIO.OUT)
        GPIO.add_event_detect(gpio_btn_pin, GPIO.RISING, callback=self.on_push, bouncetime=200)

    def on_push(self, channel):
        time.sleep(0.01)
        if not GPIO.input(self._gpio_pin):
            return
        print("Button {} pushed.".format(self._name))
        if self._on_push is not None:
            self._on_push(channel)

    def set_on_push(self, on_push):
        self._on_push = on_push

    def switch_led(self, state: bool):
        GPIO.output(self._gpio_led_pin, _output_dict[state])

    def turn_on_led(self):
        self.switch_led(True)

    def turn_off_led(self):
        self.switch_led(False)
