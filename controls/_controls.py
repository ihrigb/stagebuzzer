from ._button import Button
from display import Display, ButtonLights

_up_button_pin = 5
_left_button_pin = 27
_down_button_pin = 9
_right_button_pin = 17
_up_led_pin = 11
_left_led_pin = 22
_down_led_pin = 10
_right_led_pin = 6


class Controls:
    def __init__(self, display: Display, button_lights: ButtonLights):
        self._up_button = Button("up", _up_button_pin, _up_led_pin, lambda ch: display.up())
        self._left_button = Button("esc", _left_button_pin, _left_led_pin, lambda ch: display.esc())
        self._down_button = Button("down", _down_button_pin, _down_led_pin, lambda ch: display.down())
        self._right_button = Button("ok", _right_button_pin, _right_led_pin, lambda ch: display.ok())

        button_lights.set_up_hook(lambda state: self._up_button.switch_led(state))
        button_lights.set_left_hook(lambda state: self._left_button.switch_led(state))
        button_lights.set_down_hook(lambda state: self._down_button.switch_led(state))
        button_lights.set_right_hook(lambda state: self._right_button.switch_led(state))
