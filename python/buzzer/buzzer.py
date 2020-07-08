from .buzzer_callback import BuzzerCallback


class Buzzer:
    buzzer_callbacks = set()

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def buzz(self):
        for buzzer_callback in self.buzzer_callbacks:
            buzzer_callback.on_buzz(self)

    def register_buzzer_callback(self, buzzer_callback: BuzzerCallback):
        self.buzzer_callbacks.add(buzzer_callback)

    def unregister_buzzer_callback(self, buzzer_callback: BuzzerCallback):
        self.buzzer_callbacks.remove(buzzer_callback)
