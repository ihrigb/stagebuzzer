from .view import View
from .display import Display


class SubMenu:
    def __init__(self, name: str, view_name: str):
        self._name = name
        self._view_name = view_name

    def name(self) -> str:
        return self._name

    def view_name(self) -> str:
        return self._view_name


general_submenu = SubMenu("General", "general_menu_view")
dmx_submenu = SubMenu("DMX", "dmx_menu_view")
audio_submenu = SubMenu("Audio", "audio_menu_view")
relay_submenu = SubMenu("Relay", "relay_menu_view")
menu_view_name = "menu_view"
menu_list = [general_submenu, dmx_submenu, audio_submenu, relay_submenu]


class MenuView(View):
    _top: int = 0
    _cursor: int = 0

    def name(self):
        return menu_view_name

    def up(self, display: Display):
        if self._cursor > 0:
            self._cursor -= 1
            self.draw()
        elif self._cursor == 0 and self._top > 0:
            self._top -= 1
            self.draw()

    def down(self, display: Display):
        if self._cursor < 2:
            self._cursor += 1
            self.draw()
        elif self._cursor == 2 and self._top < 1:
            self._top += 1
            self.draw()

    def esc(self, display: Display):
        display.switch_view("main_view")

    def ok(self, display: Display):
        active_submenu = self._get_active_submenu()
        display.switch_view(active_submenu.view_name())

    def draw(self):
        self.write_line(0, "Menu")
        for i in range(self._top, self._top + 3):
            line_number = i - self._top
            line = ""
            if self._cursor == line_number:
                line += "> "
            else:
                line += "  "
            line += menu_list[i].name()
            self.write_line(line_number + 1, line)
        self.flush()

    def _get_active_submenu(self) -> SubMenu:
        return menu_list[self._cursor + self._top]
