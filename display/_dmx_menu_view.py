from ._button_lights import ButtonLights
from ._view import View
from ._display import Display
from config import DmxConfig


dmx_menu_view_name = "dmx_menu_view"
active_cursor_value = 1
buzzer_1_cursor_value = 2
buzzer_2_cursor_value = 3
min_cursor_value = active_cursor_value
max_cursor_value = buzzer_2_cursor_value


class DmxMenuView(View):

    _cursor: int = min_cursor_value

    def __init__(self, button_lights: ButtonLights, dmx_config: DmxConfig):
        super().__init__(button_lights)
        self._dmx_config = dmx_config

    def name(self):
        return dmx_menu_view_name

    def esc(self, display: Display):
        display.switch_view("menu_view")

    def up(self, display: Display):
        if self._cursor > min_cursor_value:
            self._cursor -= 1
            self.draw()

    def down(self, display: Display):
        if self._cursor < max_cursor_value:
            self._cursor += 1
            self.draw()

    def ok(self, display: Display):
        if self._cursor == active_cursor_value:
            self._dmx_config.set_active(not self._dmx_config.get_active())
            self.draw()
        elif self._cursor == buzzer_1_cursor_value:
            display.switch_view("dmx_menu_buzzer_1_view")
        elif self._cursor == buzzer_2_cursor_value:
            display.switch_view("dmx_menu_buzzer_2_view")

    def draw(self):
        self.write_line(0, "DMX Config")

        line1: str
        if self._cursor == active_cursor_value:
            line1 = "> "
        else:
            line1 = "  "
        line1 += "Active: "
        if self._dmx_config.get_active():
            line1 += "yes"
        else:
            line1 += "no"
        self.write_line(1, line1)

        line2: str
        if self._cursor == buzzer_1_cursor_value:
            line2 = "> "
        else:
            line2 = "  "
        line2 += "Buzzer 1"
        self.write_line(2, line2)

        line3: str
        if self._cursor == buzzer_2_cursor_value:
            line3 = "> "
        else:
            line3 = "  "
        line3 += "Buzzer 2"
        self.write_line(3, line3)

        self.flush()
