from ._button import Button
from display import Display


class Controls:
    def __init__(self, display: Display):
        self._up_button = Button(6, lambda ch: display.up())
        self._left_button = Button(19, lambda ch: display.esc())
        self._down_button = Button(13, lambda ch: display.down())
        self._right_button = Button(26, lambda ch: display.ok())
