from .file import File
from ._osfile import OsFile


def root() -> File:
    return OsFile("/home/ihrigb")
