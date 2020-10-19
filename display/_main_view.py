from ._button_lights import ButtonLights
from ._view import View
from ._display import Display


main_view_name = "main_view"


class MainView(View):
    def __init__(self, button_lights: ButtonLights):
        super().__init__(button_lights)

    def name(self):
        return main_view_name

    def ok(self, display: Display):
        display.switch_view("menu_view")

    def draw(self):
        self.write_line(0, "Stage Buzzer")
        self.write_line(1, "Buzzer 1")
        self.write_line(2, "Buzzer 2")
        self.write_line(3, "Version 0.1")

        self.set_button_lights(ok=True)

        self.flush()
