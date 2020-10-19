class Display:
    _views: dict = dict()
    _current_view = None

    def __init__(self, views: list):
        for view in views:
            self._views[view.name()] = view

    def start(self):
        self.switch_view("main_view")

    def switch_view(self, name: str):
        view = self._views.get(name)
        if view is None:
            pass
        self._current_view = view
        self._current_view.draw()

    def ok(self):
        self._current_view.ok(self)

    def esc(self):
        self._current_view.esc(self)

    def up(self):
        self._current_view.up(self)

    def down(self):
        self._current_view.down(self)
