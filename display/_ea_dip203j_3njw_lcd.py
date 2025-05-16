from ._lcd import Lcd
import RPi.GPIO as GPIO
from RPLCD import CharLCD
import atexit

# GPIO.setmode(GPIO.BOARD)
# lcd = CharLCD(pin_rs=26, pin_rw=7, pin_e=24, pins_data=[16, 12, 10, 8], numbering_mode=GPIO.BOARD, cols=20, rows=4,
#              dotsize=8)


class EaDip203J4Nlw(Lcd):

    _lines: list = ["", "", "", ""]
    _lcd = CharLCD(pin_rs=18, pin_rw=23, pin_e=24, pins_data=[25, 8, 7, 12], numbering_mode=GPIO.BCM, cols=20, rows=4,
                   dotsize=8)
    
    def __init__(self) -> None:
        super().__init__()

    def write_line(self, num: int, value: str):
        self._lines[num] = value

    def flush(self):
        self._lcd.clear()
        for row, value in enumerate(self._lines):
            target_row = row
            if row == 1:
                target_row = 2
            elif row == 2:
                target_row = 1
            self._lcd.cursor_pos = (target_row, 0)
            self._lcd.write_string(value)
