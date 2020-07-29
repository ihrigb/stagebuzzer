from ._view import View
from ._display import Display
from config import GeneralConfig

general_menu_view_name = "general_menu_view"


class GeneralMenuView(View):

    _edit_mode = False

    def __init__(self, general_config: GeneralConfig):
        self._general_config = general_config

    def name(self):
        return general_menu_view_name

    def esc(self, display: Display):
        if self._edit_mode:
            self._edit_mode = False
            self.draw()
        else:
            display.switch_view("menu_view")

    def ok(self, display: Display):
        if not self._edit_mode:
            self._edit_mode = True
            self.draw()

    def up(self, display: Display):
        if self._edit_mode:
            self._general_config.set_hold_time(self._general_config.get_hold_time() + 1)
            self.draw()

    def down(self, display: Display):
        if self._edit_mode:
            self._general_config.set_hold_time(self._general_config.get_hold_time() - 1)
            self.draw()

    def draw(self):
        self.write_line(0, "General Config")

        line1 = ""
        if self._edit_mode:
            line1 += "  "
        else:
            line1 += "> "
        line1 += "Hold Time: {:02d} s".format(self._general_config.get_hold_time())
        if self._edit_mode:
            line1 += " <"
        self.write_line(1, line1)
        self.write_line(2, "")
        self.write_line(3, "")
        self.flush()
