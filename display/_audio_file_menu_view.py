from ._button_lights import ButtonLights
from ._lcd import Lcd
from ._view import View
from ._display import Display
from config import AudioConfig
from usbdrive import File, root

audio_file_menu_view_name = "audio_file_menu_view"
parent_cursor_value = 1
min_cursor_value = 1


def sorted_children(file: File) -> list:
    children = sorted(file.get_children(), key=lambda f: f.get_name().lower())
    children.insert(0, file.parent())
    return children


def file_name(file: File, is_parent: bool = False) -> str:
    name = file.get_name()
    if is_parent:
        name = ".."
    if file.is_directory():
        name += "/"
    return name


class AudioFileMenuView(View):

    _cursor: int = 0
    _top: int = 0
    _max_cursor_value = 3
    _cwd: File = None

    def __init__(self, lcd: Lcd, button_lights: ButtonLights, audio_config: AudioConfig):
        super().__init__(lcd, button_lights)
        self._audio_config = audio_config
        self._init()

    def _init(self):
        file: File = None
        if self._cwd is None:
            file = self._audio_config.get_audio_file()
            if file is not None and file.exists():
                self._cwd = file.parent()
            else:
                self._cwd = root()
        dir_files = sorted_children(self._cwd)
        index = 0
        if self._is_in_configured_cwd() and file is not None and file.exists():
            index = dir_files.index(file) or 0
        if index == 0:
            self._top = 0
            self._cursor = 1
        else:
            self._top = index
            self._cursor = 1
        len_files = len(dir_files)
        self._max_cursor_value = min(3, len_files + 1)

    def name(self):
        return audio_file_menu_view_name

    def esc(self, display: Display):
        display.switch_view("audio_menu_view")

    def up(self, display: Display):
        if self._cursor > min_cursor_value:
            self._cursor -= 1
            self.draw()
        elif self._cursor == min_cursor_value and self._top > 0:
            self._top -= 1
            self.draw()

    def down(self, display: Display):
        if self._cursor < self._max_cursor_value:
            self._cursor += 1
            self.draw()
        elif self._cursor == 3 and (self._top + self._cursor - 1) < len(sorted_children(self._cwd)):
            self._top += 1
            self.draw()

    def ok(self, display: Display):
        current_file = sorted_children(self._cwd)[self._top + self._cursor - 1]
        if current_file.is_directory():
            self._cwd = current_file
            self._init()
            self.draw()
        else:
            self._audio_config.set_audio_file(current_file)

    def draw(self):
        self.write_line(0, "Audio File")

        cwd_children = sorted_children(self._cwd)

        line1 = ""
        if self._cursor == 1:
            line1 += "> "
        else:
            line1 += "  "
        line1 += file_name(cwd_children[self._top], is_parent=(self._top == 0))
        self.write_line(1, line1)

        line2 = ""
        if len(cwd_children) > 1:
            if self._cursor == 2:
                line2 += "> "
            else:
                line2 += "  "
            line2 += file_name(cwd_children[self._top + 1])
        self.write_line(2, line2)

        line3 = ""
        if len(cwd_children) > 2:
            if self._cursor == 3:
                line3 += "> "
            else:
                line3 += "  "
            line3 += file_name(cwd_children[self._top + 2])
        self.write_line(3, line3)

        self.flush()

    def _item_at_cursor(self) -> File:
        cwd_children = self._cwd.get_children()
        return cwd_children[self._top + self._cursor - 1]

    def _is_in_configured_cwd(self) -> bool:
        file = self._audio_config.get_audio_file()
        if file is None:
            return False
        if self._cwd is None:
            return False
        return file.parent().get_absolute_path() == self._cwd.get_absolute_path()
