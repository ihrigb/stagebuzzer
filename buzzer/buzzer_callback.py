from ._buzzer import Buzzer


class BuzzerCallback:
    def on_buzz(self, buzzer: Buzzer):
        pass

    def reset(self):
        pass
