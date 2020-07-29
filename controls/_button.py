import RPi.GPIO as GPIO


class Button:
    def __init__(self, name: str, gpio_pin: int, on_push):
        self._name = name
        self._on_push = on_push

        GPIO.setup(gpio_pin, GPIO.IN)
        GPIO.add_event_detect(gpio_pin, GPIO.RISING, callback=self.on_push, bouncetime=200)

    def on_push(self, channel):
        print("Button {} pushed.".format(self._name))
        if self._on_push is not None:
            self._on_push(channel)

    def set_on_push(self, on_push):
        self._on_push = on_push

