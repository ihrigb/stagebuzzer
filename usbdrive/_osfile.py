from ._file import File
from os import listdir, sep
from os.path import isdir, exists, dirname


class OsFile(File):
    def __init__(self, path: str):
        self._path = path

    def is_directory(self) -> bool:
        return isdir(self._path)

    def get_absolute_path(self):
        return self._path

    def get_name(self):
        return self._path.rsplit(sep, 1)[-1]

    def get_children(self, extension: str = None) -> list:
        if not self.is_directory():
            return list()
        paths = listdir(self._path)
        paths = map(lambda p: "{}{}{}".format(self._path, sep, p), paths)
        if extension is not None:
            paths = filter(lambda p: isdir(p) or p.endswith(extension), paths)
        return [OsFile(path) for path in paths]

    def exists(self) -> bool:
        return exists(self._path)

    def parent(self):
        return OsFile(dirname(self._path))
