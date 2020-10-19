from typing import Callable


class ButtonLights:
    _left_hook = lambda state: state
    _right_hook = lambda state: state
    _up_hook = lambda state: state
    _down_hook = lambda state: state

    def enable_left(self):
        self.set_left(True)

    def enable_right(self):
        self.set_right(True)

    def enable_up(self):
        self.set_up(True)

    def enable_down(self):
        self.set_down(True)

    def disable_left(self):
        self.set_left(False)

    def disable_right(self):
        self.set_right(False)

    def disable_up(self):
        self.set_up(False)

    def disable_down(self):
        self.set_down(False)

    def set(self, left: False, right: False, up: False, down: False):
        self.set_left(left)
        self.set_right(right)
        self.set_up(up)
        self.set_down(down)

    def set_left(self, state: bool):
        self._left_hook(state)

    def set_right(self, state: bool):
        self._right_hook(state)

    def set_up(self, state: bool):
        self._up_hook(state)

    def set_down(self, state: bool):
        self._down_hook(state)

    def set_up_hook(self, hook: Callable[[bool], None]):
        self._up_hook = hook

    def set_down_hook(self, hook: Callable[[bool], None]):
        self._down_hook = hook

    def set_left_hook(self, hook: Callable[[bool], None]):
        self._left_hook = hook

    def set_right_hook(self, hook: Callable[[bool], None]):
        self._right_hook = hook
