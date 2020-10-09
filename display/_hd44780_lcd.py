from ._lcd import Lcd
import RPi.GPIO as GPIO
from RPLCD import CharLCD

# GPIO.setmode(GPIO.BOARD)
# lcd = CharLCD(pin_rs=26, pin_rw=7, pin_e=24, pins_data=[16, 12, 10, 8], numbering_mode=GPIO.BOARD, cols=20, rows=4,
#              dotsize=8)
GPIO.setmode(GPIO.BCM)


class HD44780Lcd(Lcd):

    _lines: list = ["", "", "", ""]
    _lcd = CharLCD(pin_rs=7, pin_rw=4, pin_e=8, pins_data=[23, 18, 15, 14], numbering_mode=GPIO.BCM, cols=20, rows=4,
                  dotsize=8)

    def write_line(self, num: int, value: str):
        self._lines[num] = value

    def flush(self):
        self._lcd.clear()
        for row, value in enumerate(self._lines):
            self._lcd.cursor_pos = (row, 0)
            self._lcd.write_string(value)
