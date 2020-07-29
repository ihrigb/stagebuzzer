import RPi.GPIO as GPIO


class Button:
    def __init__(self, gpio_pin: int, on_push):
        self._on_push = on_push

        GPIO.setup(gpio_pin, GPIO.IN)
        GPIO.add_event_detect(gpio_pin, GPIO.RISING, callback=self._on_push)

    def set_on_push(self, on_push):
        self._on_push = on_push

