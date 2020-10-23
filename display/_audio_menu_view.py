from ._button_lights import ButtonLights
from ._view import View
from ._display import Display
from config import AudioConfig

audio_menu_view_name = "audio_menu_view"
active_cursor_value = 1
file_cursor_value = 2
min_cursor_value = active_cursor_value
max_cursor_value = file_cursor_value


class AudioMenuView(View):

    _cursor: int = 1

    def __init__(self, button_ligts: ButtonLights, audio_config: AudioConfig):
        super().__init__(button_ligts)
        self._audio_config = audio_config

    def name(self):
        return audio_menu_view_name

    def up(self, display: Display):
        # if self._cursor > min_cursor_value:
        #    self._cursor -= 1
        #    self.draw()
        pass

    def down(self, display: Display):
        # if self._cursor < max_cursor_value:
        #    self._cursor += 1
        #    self.draw()
        pass

    def ok(self, display: Display):
        # if self._cursor == active_cursor_value:
        self._audio_config.set_active(not self._audio_config.get_active())
        self.draw()
        # elif self._cursor == file_cursor_value:
        #    display.switch_view("audio_file_menu_view")

    def esc(self, display: Display):
        display.switch_view("menu_view")

    def draw(self):
        self.write_line(0, "Audio Config")

        line1 = ""
        if self._cursor == active_cursor_value:
            line1 += "> "
        else:
            line1 += "  "
        line1 += "Active: "
        if self._audio_config.get_active():
            line1 += "yes"
        else:
            line1 += "no"
        self.write_line(1, line1)

        line2 = ""
        # if self._cursor == file_cursor_value:
        #    line2 += "> "
        # else:
        #    line2 += "  "
        line2 += "File"
        self.write_line(2, line2)

        self.write_line(3, "")

        self.set_button_lights(esc=True, ok=True)

        self.flush()
