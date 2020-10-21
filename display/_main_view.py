from ._button_lights import ButtonLights
from ._view import View
from ._display import Display
import buzzer as bzr
import logging


main_view_name = "main_view"


class MainView(View, bzr.BuzzerCallback):

    _buzzer_1_enabled = False
    _buzzer_2_enabled = False

    def __init__(self, button_lights: ButtonLights):
        super().__init__(button_lights)

    def name(self):
        return main_view_name

    def ok(self, display: Display):
        display.switch_view("menu_view")

    def draw(self):
        self.write_line(0, "Stage Buzzer")
        self.write_line(1, "")
        self.write_line(2, "Buzzer 1{}".format(' <<<' if self._buzzer_1_enabled is True else ''))
        self.write_line(3, "Buzzer 2{}".format(' <<<' if self._buzzer_1_enabled is True else ''))

        self.set_button_lights(ok=True)

        self.flush()

    def on_buzz(self, buzzer: str):
        logging.debug('Buzzer callback for main view called.')
        if buzzer == '1':
            self._buzzer_1_enabled = True
        if buzzer == '2':
            self._buzzer_2_enabled = True
        self.draw()

    def reset(self):
        self._buzzer_1_enabled = False
        self._buzzer_2_enabled = False
