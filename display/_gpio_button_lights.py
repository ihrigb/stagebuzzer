import RPi.GPIO as GPIO
from ._button_lights import ButtonLights
from controls import Bu

LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"


class GpioButtonLights(ButtonLights):

    def __init__(self, button_up: Button):
        self._state = dict()
        self._state[LEFT] = False
        self._state[RIGHT] = False
        self._state[UP] = False
        self._state[DOWN] = False

        GPIO.setup(GPIO_LEFT, GPIO.OUT)
        GPIO.setup(GPIO_RIGHT, GPIO.OUT)
        GPIO.setup(GPIO_UP, GPIO.OUT)
        GPIO.setup(GPIO_DOWN, GPIO.OUT)

        self.flush()

    def set_left(self, state: bool):
        self._state[LEFT] = state

    def set_right(self, state: bool):
        self._state[RIGHT] = state

    def set_up(self, state: bool):
        self._state[UP] = state

    def set_down(self, state: bool):
        self._state[DOWN] = state

    def flush(self):
        GPIO.output(GPIO_LEFT, self._state[LEFT])
        GPIO.output(GPIO_RIGHT, self._state[RIGHT])
        GPIO.output(GPIO_UP, self._state[UP])
        GPIO.output(GPIO_DOWN, self._state[DOWN])
