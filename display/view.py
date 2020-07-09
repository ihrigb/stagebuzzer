from .display import Display
from .lcd import Lcd


class View:

    _led = Lcd()

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
        self._led.write_line(num, value)

    def flush(self):
        self._led.flush()
