from ._display import Display
from ._hd44780_lcd import HD44780Lcd


class View:

    _lcd = HD44780Lcd()

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

    def flush(self):
        self._lcd.flush()
