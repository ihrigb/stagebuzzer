class ButtonLights:
    def enable_left(self):
        self.set_left(True)

    def enable_right(self):
        self.set_right(True)

    def enable_up(self):
        self.set_up(True)

    def enable_down(self):
        self.set_down(True)

    def disable_left(self):
        self.set_left(False)

    def disable_right(self):
        self.set_right(False)

    def disable_up(self):
        self.set_up(False)

    def disable_down(self):
        self.set_down(False)

    def set(self, left: False, right: False, up: False, down: False):
        self.set_left(left)
        self.set_right(right)
        self.set_up(up)
        self.set_down(down)

    def set_left(self, state: bool):
        pass

    def set_right(self, state: bool):
        pass

    def set_up(self, state: bool):
        pass

    def set_down(self, state: bool):
        pass

    def flush(self):
        pass
