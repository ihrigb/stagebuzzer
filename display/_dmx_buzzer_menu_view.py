from ._button_lights import ButtonLights
from ._lcd import Lcd
from ._view import View
from ._display import Display
from config import DmxConfig


address_cursor_value = 2
value_cursor_value = 3
min_cursor = address_cursor_value
max_cursor = value_cursor_value


class DmxBuzzerMenuView(View):
    _cursor = min_cursor
    _edit_mode = False

    def __init__(self, lcd: Lcd, button_lights: ButtonLights, name: str, buzzer_name: str, dmx_config: DmxConfig):
        super().__init__(lcd, button_lights)
        self._name = name
        self._buzzer_name = buzzer_name
        self._dmx_config = dmx_config

    def name(self):
        return self._name

    def esc(self, display: Display):
        if self._edit_mode:
            self._edit_mode = False
            self.draw()
        else:
            display.switch_view("dmx_menu_view")

    def up(self, display: Display):
        if self._edit_mode:
            self._edit_up()
            self.draw()
        elif self._cursor > min_cursor:
            self._cursor -= 1
            self.draw()

    def down(self, display: Display):
        if self._edit_mode:
            self._edit_down()
            self.draw()
        elif self._cursor < max_cursor:
            self._cursor += 1
            self.draw()

    def ok(self, display: Display):
        if not self._edit_mode:
            self._edit_mode = True
            self.draw()

    def _edit_up(self):
        if self._cursor == address_cursor_value:
            self._dmx_config.set_dmx_address(self._buzzer_name, self._dmx_config.get_dmx_address(self._buzzer_name) + 1)
        elif self._cursor == value_cursor_value:
            self._dmx_config.set_dmx_value(self._buzzer_name, self._dmx_config.get_dmx_value(self._buzzer_name) + 1)

    def _edit_down(self):
        if self._cursor == address_cursor_value:
            self._dmx_config.set_dmx_address(self._buzzer_name, self._dmx_config.get_dmx_address(self._buzzer_name) - 1)
        elif self._cursor == value_cursor_value:
            self._dmx_config.set_dmx_value(self._buzzer_name, self._dmx_config.get_dmx_value(self._buzzer_name) - 1)

    def draw(self):
        self.write_line(0, "DMX Config Buzzer {name}".format(name=self._buzzer_name))
        self.write_line(1, "")

        line2 = ""
        if self._cursor == address_cursor_value and not self._edit_mode:
            line2 += "> "
        else:
            line2 += "  "
        line2 += "Address: "
        line2 += "{:03d}".format(self._dmx_config.get_dmx_address(self._buzzer_name))
        if self._cursor == address_cursor_value and self._edit_mode:
            line2 += " <"
        self.write_line(2, line2)

        line3 = ""
        if self._cursor == value_cursor_value and not self._edit_mode:
            line3 += "> "
        else:
            line3 += "  "
        line3 += "Value:   "
        line3 += "{:03d}".format(self._dmx_config.get_dmx_value(self._buzzer_name))
        if self._cursor == value_cursor_value and self._edit_mode:
            line3 += " <"
        self.write_line(3, line3)

        self.flush()
