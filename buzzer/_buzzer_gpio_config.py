class BuzzerGpioConfig:
    def __init__(self, pin_a: int, pin_b: int):
        self._pin_a = pin_a
        self._pin_b = pin_b

    def get_pin_a(self):
        return self._pin_a

    def get_pin_b(self):
        return self._pin_b
