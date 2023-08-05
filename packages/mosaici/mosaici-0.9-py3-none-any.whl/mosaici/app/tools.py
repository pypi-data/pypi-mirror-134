from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
import os
import time
import json

from enum import Enum

# IMPORT COLORAMA
from colorama import init, Fore, Back, Style

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

# Change Regular Ansi Color Algorithm To `Coloroma` Cross Platform Terminal Color

# COLORAMA INITIALIZE
init(autoreset=True)

# COLOR ENUM CLASS
class Color(Enum):
    TITLE = f"{Fore.CYAN}{Style.DIM}"
    RESULT = f"{Fore.BLACK}{Back.LIGHTBLACK_EX}"
    WORK = f"{Fore.BLUE}{Style.BRIGHT}"
    DONE = f"{Fore.WHITE}{Style.DIM}"
    SPACER = f"{Fore.LIGHTBLACK_EX}{Style.DIM}"
    WARNING = f"{Fore.YELLOW}{Style.BRIGHT}"
    ERROR = f"{Fore.WHITE}{Back.RED}"
    TIME = f"{Fore.LIGHTBLACK_EX}"
    RESET = f"{Style.RESET_ALL}"
    OTHER = f"{Fore.BLUE}"

    # Get Color By Name
    @classmethod
    def color(cls, name: str) -> str:
        attr = getattr(cls, name.upper(), cls.OTHER)
        return attr.value

    # Colorize String
    @classmethod
    def colorize(cls, txt: str, color_name: str | Color) -> str:
        if isinstance(color_name, Color):
            return f"{color_name.value}{txt}"
        else:
            return f"{cls.color(color_name)}{txt}"


# JSON
class Json:

    @staticmethod
    def load(path: str | os.PathLike) -> dict:
        path = os.path.realpath(path)
        with open(path, 'r') as f:
            return json.load(f)

    @staticmethod
    def save(obj: dict, path: str | os.PathLike) -> None:
        path = os.path.realpath(path)
        with open(path, 'w') as f:
            json.dump(obj, f, indent=6)

    @staticmethod
    def update(obj: dict, path: str | os.PathLike) -> None:
        path = os.path.realpath(path)
        with open(path, 'r') as f:
            temp = json.load(f)

        temp.update(obj)

        with open(path, 'w') as f:
            json.dump(temp, f, indent=6)


# PATH JOIN
def path_join(path: str | os.PathLike, *paths: str | os.PathLike) -> os.PathLike:
    path = os.path.join(path, *paths)
    return os.path.realpath(path)

# BASE NAME
def basename(path: str | os.PathLike) -> str:
    return os.path.basename(path)

# GET TERMINAL SIZE
def get_terminal_size() -> tuple[int, int]:
    return os.get_terminal_size()

# TIME
def monotonic() -> float:
    return time.monotonic()

# PRINT COLOR SUPPROT
def color_print(txt: str, color: Color | str = None, end: str = '\n', flush: bool = False) -> None:
    if color:
        txt = Color.colorize(txt, color)
    print(txt, end=end, flush=flush)

# GET VALID TERMINAL COLUMN SIZE
def icol(padding: int = 0) -> int:
    col, _ = get_terminal_size()
    col -= 1
    col -= padding
    return col

# TO CENTER
def center(txt: str, fillchar: str = ' ', padding: int = 0, width:int = None) -> str:
    if width is None:
        width = icol(padding)
    return txt.center(width, fillchar)

# MAKE SPACER
def spacer(space_char: str = '-', many: int = None, padding: int = 0) -> str:
    col = icol(padding)
    
    if many is None:
        many = col // 2

    txt = space_char * many
    txt = Color.colorize(txt, Color.SPACER)
    return center(txt, width=col)

# MAKE ERROR
def error(err: Exception, more: str = None) -> str:
    txt = f"{type(err).__qualname__}\n\t{repr(err)}"
    if more:
        txt += f'\n\t** {more}'
    return Color.colorize(txt, Color.ERROR)




__dir__ = (
    "Color",
    "Json",
    "path_join",
    "basename",
    "get_terminal_size",
    "monotonic",
    "color_print",
    "icol",
    "center",
    "spacer",
    "error",
    )
