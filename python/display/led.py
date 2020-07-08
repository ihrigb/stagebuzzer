class Led:

    _lines: list = ["", "", "", ""]

    def write_line(self, num: int, value: str):
        self._lines[num] = value[0:20]

    def flush(self):
        print()
        print("#" * 20)
        for line in self._lines:
            print(line)
        print("#" * 20)
