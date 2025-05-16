import RPi.GPIO as GPIO

_relay_pins = dict()
_relay_pins["1"] = 16
_relay_pins["2"] = 20


class RelayOutput:
    def __init__(self) -> None:
        for pin in _relay_pins.values():
            GPIO.setup(pin, GPIO.OUT)

    def enable_relay(self, name: str):
        pin = _relay_pins[name]
        GPIO.output(pin, True)

    def reset(self):
        for pin in _relay_pins.values():
            GPIO.output(pin, False)
