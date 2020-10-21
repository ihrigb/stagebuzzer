from ._button_lights import ButtonLights
from ._view import View
from ._display import Display
from information import get_ip_address

information_menu_view_name = "information_menu_view"


class InformationMenuView(View):
    def __init__(self, button_lights: ButtonLights):
        super().__init__(button_lights)

    def name(self):
        return information_menu_view_name

    def esc(self, display: Display):
        display.switch_view("menu_view")

    def draw(self):
        self.write_line(0, "Information")
        self.write_line(1, "")
        self.write_line(2, "IP: {}".format(get_ip_address()))
        self.write_line(3, "Version: 0.1")

        self.set_button_lights(esc=True)

        self.flush()
