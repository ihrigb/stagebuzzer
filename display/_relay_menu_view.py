from ._view import View
from ._display import Display
from config import RelayConfig


relay_menu_view_name: str = "relay_menu_view"


class RelayMenuView(View):

    def __init__(self, relay_config: RelayConfig):
        self._relay_config = relay_config

    def name(self):
        return relay_menu_view_name

    def esc(self, display: Display):
        display.switch_view("menu_view")

    def ok(self, display: Display):
        self._switch_state()

    def draw(self):
        self.write_line(0, "Relay Config")
        line = "> Active: "
        if self._relay_config.get_active():
            line += "yes"
        else:
            line += "no"
        self.write_line(1, line)
        self.write_line(2, "")
        self.write_line(3, "")

        self.set_button_lights(ok=True, esc=True)

        self.flush()

    def _switch_state(self):
        self._relay_config.set_active(not self._relay_config.get_active())
        self.draw()
