from ._button import Button
from display import Display


class Controls:
    def __init__(self, display: Display):
        self._up_button = Button(31, lambda: display.up())
        self._left_button = Button(33, lambda: display.esc())
        self._down_button = Button(35, lambda: display.down())
        self._right_button = Button(36, lambda: display.ok())
