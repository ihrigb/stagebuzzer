import RPi.GPIO as GPIO
from RPLCD import CharLCD

GPIO.setmode(GPIO.BCM)
lcd = CharLCD(pin_rs=7, pin_rw=4, pin_e=8, pins_data=[23, 18, 15, 14], numbering_mode=GPIO.BCM, cols=20, rows=4,
              dotsize=8)


class Lcd:

    _lines: list = ["", "", "", ""]

    def write_line(self, num: int, value: str):
        self._lines[num] = value[0:20]

    def flush(self):
        for row, value in enumerate(self._lines):
            lcd.cursor_pos = (row, 0)
            lcd.write_string(value)
