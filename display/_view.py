from ._button_lights import ButtonLights
from ._display import Display
from ._ea_dip203j_3njw_lcd import EaDip203J4Nlw
from ._hd44780_lcd import HD44780Lcd


class View:

    _lcd = HD44780Lcd()

    def __init__(self, button_lights: ButtonLights):
        self._button_ligts = button_lights

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
