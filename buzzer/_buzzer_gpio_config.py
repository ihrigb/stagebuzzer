class BuzzerGpioConfig:
    def __init__(self, pin_1: int, pin_2: int):
        self._pin_1 = pin_1
        self._pin_2 = pin_2

    def get_pin_1(self):
        return self._pin_1

    def get_pin_2(self):
        return self._pin_2
