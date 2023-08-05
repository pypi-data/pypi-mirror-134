from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
from enum import Enum
from functools import lru_cache

# IMPORT LOCAL
from mosaici.exceptions import *
from mosaici.pattern import Convertor


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

# VALID MODE TYPE
class ModeType(Enum):
    """
    ModeType - Valid Mode Mosaic Standard Type File - Instance of Enum
    Mode:
        TXT -> Text File [value 'T']
        BIN -> Binarray File [value 'B']

    Action:
        READ -> Read File Only [value 'R']
        WRITE -> Write File Only [value 'W']
        UPDATE -> Update File Read & Write [value 'U']
    """
    TXT = 'T'
    BIN = 'B'
    READ = 'R'
    WRITE = 'W'
    UPDATE = 'U'


# MODE NAME - CHECK MODE TYPE
class ModeName:

    WRITE_BIN: tuple[str, ...] = ('wb', 'ab')
    READ_BIN: tuple[str, ...] = ('rb',)
    UPDATE_BIN: tuple[str, ...] = ('rb+', 'r+b')

    WRITE_TXT: tuple[str, ...] = ('w', 'a', 'wt', 'at')
    READ_TXT: tuple[str, ...] = ('r', 't', 'rt')
    UPDATE_TXT: tuple[str, ...] = ('r+', 'r+t', 'rt+')

    def __init__(self, mode: str) -> None:
        """
        Initialize - ModeName
        Create File Mode To ModeName
        const:
            WRITE_BIN [tuple[str,...]]: [All Write Binarray Mode]
            READ_BIN [tuple[str,...]]: [All Read Binarray Mode]
            UPDATE_BIN [tuple[str,...]]: [All Update Binarray Mode]
            WRITE_TXT [tuple[str,...]]: [All Write Text Mode]
            READ_TXT [tuple[str,...]]: [All Read Text Mode]
            UPDATE_TXT [tuple[str,...]]: [All Update Text Mode]

        args:
            mode [str]: [File Mode]

        --- --- --- ---
        name spaces:
            file_mode [str]: [real file mode]
            mode_type [ModeType]: [ModeType From Mode]
            action_mode [ModeType]: [Read or Write or Update]
            can_write [bool]: [Mode Write Available]
            can_read [bool]: [Mode Read Available]
        """

        self.file_mode = mode
        self.mode_type = None
        self.action_mode = None
        self.can_write: bool = None
        self.can_read: bool = None

        self._mode_type()
        self._action_mode()
        self._can_do()

    def _mode_type(self) -> None:
        """
        Convert FileMode to ModeType
        """
        _bin = {*self.READ_BIN, *self.WRITE_BIN, *self.UPDATE_BIN}
        _txt = {*self.READ_TXT, *self.WRITE_TXT, *self.UPDATE_TXT}

        if self.file_mode in _bin:
            self.mode_type = ModeType.BIN
            del _bin, _txt

        elif self.file_mode in _txt:
            self.mode_type = ModeType.TXT
            del _bin, _txt

        else:
            del _bin, _txt
            raise ModeNotExistsError

    def _action_mode(self) -> None:
        """
        Action Mode Read or Write or Update
        """
        _read = {*self.READ_BIN, *self.READ_TXT}
        _write = {*self.WRITE_BIN, *self.WRITE_TXT}
        _update = {*self.UPDATE_BIN, *self.UPDATE_TXT}

        if self.file_mode in _read:
            self.action_mode = ModeType.READ
            del _read, _write, _update

        elif self.file_mode in _write:
            self.action_mode = ModeType.WRITE
            del _read, _write, _update

        elif self.file_mode in _update:
            self.action_mode = ModeType.UPDATE
            del _read, _write, _update

        else:
            del _read, _write, _update
            raise ActionNotExistsError

    def _can_do(self) -> None:
        """
        Can Do Write Or Read Or Both `Update`
        """
        match self.action_mode:
            case ModeType.UPDATE:
                self.can_write = True
                self.can_read = True
            case ModeType.READ:
                self.can_write = False
                self.can_read = True
            case ModeType.WRITE:
                self.can_write = True
                self.can_read = False


# PROTOCOL ABSTRACT
class BaseProtocol:
    """
    Protocol
    """
    SEPARATOR: tuple[str, bytes]
    MODETYPE: ModeType = ModeType

    def __init__(self, convertor: Convertor) -> None:
        """
        Initialize Protocol

        const:
            SEPARATOR [tuple[str, bytes]]: [Separator String and Bytes For Joining Together].
            MODETYPE [ModeType]: [Valid File Type See `ModeName` & `ModeType`]

        args:
            convertor [Convertor]: [Standard Convertor Type].
        """
        if not self.SEPARATOR:
            raise NotImplementedError

        self._convertor = convertor
        self._valid_mode= ModeName

    def __call__(self, value: int | str, type_io: str | ModeName) -> int | str:
        """
        This Method Calls For Validate Value To Protocol
        args:
            value [int | str]: [Value Must be int Or Standard String]

        return:
            [int | str]: [Validate Value With Protocol]
        """
        raise NotImplementedError

    @lru_cache(1)
    def __getitem__(self, name: str | ModeName) -> str | bytes:
        """
        Get Separator
        args:
            name [str]: [Name of separator].
                ** VALID NAMES : See `ModeName` Object

        return:
            [str | bytes]: [Separator By Name].
        """
        if isinstance(name, str):
            name = self._valid_mode(name)

        match name.mode_type:
            case self.MODETYPE.TXT:
                return self.SEPARATOR[0]
            case self.MODETYPE.BIN:
                return self.SEPARATOR[-1]

    def __repr__(self) -> str:
        return f"{type(self).__qualname__}(STR_SEPARATOR: [{self.SEPARATOR[0]}], BYTES_SEPARATOR: [{self.SEPARATOR[-1]}])"


# STANDARD WRITE PROTOCOL
class WriteProtocol(BaseProtocol):
    SEPARATOR: tuple[str, bytes] = ('', b'')    # (String Separator, Bytes Separator)

    def __init__(self) -> None:
        """
        Standard Write Protocol
        """
        super(WriteProtocol, self).__init__(Convertor())
        self._str_validate = lambda x: self._convertor.std_hex(x)
        self._byt_validate = lambda x: bytes([self._convertor.std_int(x)])

    @lru_cache(256)
    def __call__(self, value: int | str, type_io: str | ModeName) -> str | bytes:
        """
        Value To Standard Protocol For Write To File - String or Bytes.
        if `type_io` is String `Text` return Type is String.
        if `type_io` is Bytes `Binarray` return Type is Bytes.
        args:
            value [int | str]: [Value Must be int Or Standard String].
            type_io [str | ModeName]: [File Opening Mode See `ModeName` Object].

        return:
            [str | bytes]: [Standard Value String or Bytes].
        """
        if isinstance(type_io, str):
            type_io = self._valid_mode(type_io)

        match type_io.mode_type:
            case self.MODETYPE.TXT:
                return self._str_validate(value)
            case self.MODETYPE.BIN:
                return self._byt_validate(value)


# READ PROTOCOL ABSTRACT
class BaseReadProtocol(BaseProtocol):
    # (String Read Size, Bytes Read Size)
    READ_SIZE: tuple[int, int]

    def __init__(self, convertor: Convertor) -> None:
        """
        Read Protocol

        const:
            SEPARATOR [tuple[str, bytes]]: [Separator For Skiping]
            MODETYPE [ModeType]: [Valid File Type See `ModeName` & `ModeType`]
            READ_SIZE [tuple[int, int]]: [Read Size For String Or Binarray Object]
        """
        if not self.READ_SIZE:
            raise NotImplementedError

        super(BaseReadProtocol, self).__init__(convertor)

    @lru_cache(1)
    def get_config(self, name: str | ModeName) -> dict[str, str|bytes|int]:
        """
        Get Config
        args:
            name [str | ModeName]: [File Mode Name].

        return:
            [dict[str, str|int|bytes]]: [Dict Of Config Value].
                ** {'size': `read_size`, 'skip': `separator`, 'mode': `ModeName`, 'read': `ModeName.can_read`, 'write': `ModeName.can_write`}
        """
        if isinstance(name, str):
            name = self._valid_mode(name)

        match name.mode_type:
            case self.MODETYPE.TXT:
                return {'size':self.READ_SIZE[0], 'skip': self.SEPARATOR[0], 'mode': name,'read': name.can_read, 'write': name.can_write}
            case self.MODETYPE.BIN:
                return {'size':self.READ_SIZE[-1], 'skip': self.SEPARATOR[-1], 'mode': name, 'read': name.can_read, 'write': name.can_write}

    @lru_cache(1)
    def read_size(self, name: str | ModeName) -> int:
        """
        Get Read Size
        args:
            name [str | ModeName]: [File Mode Name].

        return:
            [int]: [Read Size].
        """
        if isinstance(name, str):
            name = self._valid_mode(name)

        match name.mode_type:
            case self.MODETYPE.TXT:
                return self.READ_SIZE[0]
            case self.MODETYPE.BIN:
                return self.READ_SIZE[-1]


# STANDARD READ PROTOCOL
class ReadProtocol(BaseReadProtocol):
    SEPARATOR: tuple[str, bytes] = ('', b'')
    READ_SIZE: tuple[int, int] = (2, 1)     # (String Read Size, Bytes Read Size)

    def __init__(self) -> None:
        """
        Standard Read Protocol
        ** This Object Can Only Handle Files Created With Standard Write Protocol
        """
        super(ReadProtocol, self).__init__(Convertor())

        self._str_validate = lambda x: self._convertor.std_int(x)
        self._byt_validate = lambda x: int.from_bytes(x, 'little')

    @lru_cache(256)
    def __call__(self, value: int | str | bytes, type_io: str | ModeName) -> int:
        """
        Value To Int Indexes
        args:
            value [int | str]: [Read Value From File Object With Size read_size].
            type_io [str | ModeName]: [Mode File Text Or Binarray File - See ModeName].

        return:
            [int]: [Valid Indexes]
        """
        if isinstance(type_io, str):
            type_io = self._valid_mode(type_io)

        match type_io.mode_type:
            case self.MODETYPE.TXT:
                return self._str_validate(value)
            case self.MODETYPE.BIN:
                return self._byt_validate(value)



__dir__ = ('ModeType', 'ModeName', 'BaseProtocol', 'WriteProtocol', 'BaseReadProtocol','ReadProtocol')
