from ._button_lights import ButtonLights
from ._display import Display
from ._lcd import Lcd


class View:
    def __init__(self, lcd: Lcd, button_lights: ButtonLights):
        self._button_ligts = button_lights
        self._lcd = lcd

    def name(self):
        pass

    def up(self, display: Display):
        pass

    def down(self, display: Display):
        pass

    def ok(self, display: Display):
        pass

    def esc(self, display: Display):
        pass

    def draw(self):
        pass

    def write_line(self, num: int, value: str):
        self._lcd.write_line(num, value)

    def set_button_lights(self, esc=False, ok=False, up=False, down=False):
        self._button_ligts.set(esc, ok, up, down)

    def flush(self):
        self._lcd.flush()
