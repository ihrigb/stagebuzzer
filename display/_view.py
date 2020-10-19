from ._display import Display
from ._ea_dip203j_3njw_lcd import EaDip203J4Nlw


class View:

    _lcd = EaDip203J4Nlw()

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
        pass

    def flush(self):
        self._lcd.flush()
