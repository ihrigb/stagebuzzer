from ._lcd import Lcd
import RPi.GPIO as GPIO
from RPLCD import CharLCD

#GPIO.setmode(GPIO.BOARD)
#lcd = CharLCD(pin_rs=26, pin_rw=7, pin_e=24, pins_data=[16, 12, 10, 8], numbering_mode=GPIO.BOARD, cols=20, rows=4,
#              dotsize=8)
GPIO.setmode(GPIO.BCM)
lcd = CharLCD(pin_rs=7, pin_rw=4, pin_3=8, pins_data=[23, 18, 15, 14], numbering_mode=GPIO.BCM, cols=20, rows=4,
              dotsize=8)


class HD44780Lcd(Lcd):

    _lines: list = ["", "", "", ""]

    def write_line(self, num: int, value: str):
        self._lines[num] = value[0:20]

    def flush(self):
        for row, value in enumerate(self._lines):
            lcd.clear()
            lcd.cursor_pos = (row, 0)
            lcd.write_string(value)
