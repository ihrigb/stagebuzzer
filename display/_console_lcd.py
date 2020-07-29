from ._lcd import Lcd


class ConsoleLcd(Lcd):
    _lines = ["", "", "", ""]

    def write_line(self, num: int, value: str):
        self._lines[num] = value[0:20]

    def flush(self):
        print("#" * 20)
        for line in self._lines:
            print(line)
        print("#" * 20)
