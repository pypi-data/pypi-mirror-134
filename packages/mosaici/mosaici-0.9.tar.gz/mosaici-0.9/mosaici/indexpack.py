from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
import os
from io import FileIO

# IMPORT LOCAL
from mosaici.exceptions import *
from mosaici.pattern import Wrapped, BasePattern
from mosaici.store import BaseStoreIndexes
from mosaici.protocol import BaseReadProtocol, ReadProtocol, ModeName, ModeType

# IMPORT TYPING
from typing import Iterable, Iterator

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

# TYPE ALIASES
T_INDEXES: str | list[hex|int] | tuple[hex|int, ...] | Iterable[str] | BaseStoreIndexes


# INDEXES ABSTRACT
class BaseIndexes(BasePattern):

    def __init__(self, indexes: T_INDEXES, separator: str = None) -> None:
        """
        Indexes Handler Instance of `BasePattern`
        const:
            WRAPPED [Wrapped]: [Standard Wrapper Types].
        args:
            indexes [T_INDEXES]: [indexes]
            separator [str]: [Separator if Exists in String Indexes] default is None.
                ** `None` Means Without Separator. real mean None is '' 
        """
        super(BaseIndexes, self).__init__()

        if separator in (None, ''):
            self._separator = None
        else:
            self._separator = separator

        if separator is not None and isinstance(indexes, str):
            self._indexes = indexes.split(self._separator)
        else:
            self._indexes = indexes

        # Set Wrapped Order To Store Object WRAPPED
        if isinstance(self._indexes, BaseStoreIndexes):
            self._indexes.WRAPPED = self.WRAPPED

        self._current = 0

    def _validate(self) -> tuple[str|int]:
        """
        Indexes To Tuple Of Indexes
        return:
            [tuple[str|int]]: [tuple of indexes]
        """
        if self._indexes is None:
            raise IndexesIsNotDefinedError

        if isinstance(self._indexes, (list, tuple)):
            return tuple(self._indexes)

        self._indexes = tuple(self._indexes)
        return self._indexes

    def __len__(self) -> int:
        # Store Object Support Length
        if isinstance(self._indexes, BaseStoreIndexes):
            return len(self._indexes)
        return len(self._validate())

    def __next__(self) -> int | str:
        """
        return:
            [str|int]:[Next Index From Indexes With Orderize Wrapped]
        """
        if isinstance(self._indexes, BaseStoreIndexes):
            try:
                get = next(self._indexes)
                self._current = self._indexes._current
                # Store Object Indexes Support _inorder Method And Return Ordered Value
                return get
            except StopIteration:
                raise StopIteration
            except Exception as err:
                raise err

        elif isinstance(self._indexes, str):
            try:
                get = self._indexes[self._current: (self._current + 2)]
                self._current += 2
                if get not in ('', ' ') and len(get) == 2:
                    return self._inorder(get, self.WRAPPED)
                else:
                    raise StopIteration
            except IndexError:
                raise StopIteration

        elif isinstance(self._indexes, (list, tuple)):
            try:
                get = self._indexes[self._current]
                self._current += 1
                return self._inorder(get, self.WRAPPED)
            except IndexError:
                raise StopIteration

        else:
            try:
                get = next(self._indexes)
                self._current += 1
                return self._inorder(get, self.WRAPPED)
            except (IndexError, StopIteration):
                raise StopIteration


# INDEXES FILE ABSTRACT
class BaseFileIndexes(BasePattern):
    PROTOCOL: BaseReadProtocol

    def __init__(self, file_obj: FileIO) -> None:
        """
        File Indexes Instance of BasePattern
        const:
            WRAPPED [Wrapped]: [Standard Wrapper Types]
            PROTOCOL [BaseReadProtocol]: [Read Protocol]

        args:
            file_obj [FileIO]: [File Object With 'read' method]

        ** example:
            with open(indexpath.idx, 'rb') as f:
                with FileIndexes(f) as idx:
                    for i in idx:
                        do_stuff(i)
        """
        super(BaseFileIndexes, self).__init__()
        if not self.PROTOCOL:
            raise NotImplementedError

        self._file: FileIO = file_obj
        self._mode: str = self._file.mode
        self._config: dict = self.PROTOCOL.get_config(self._mode)
        self._end = self.size()

    def size(self) -> int:
        """
        Size Of File
        """
        self._file.seek(0, 2)
        end = self._file.tell()
        self._file.seek(0,0)
        return end

    def ended(self) -> bool:
        """
        Check If Seeker in End Of File Return True
        """
        match (self._current == self._end):
            case True:
                return True
            case _:
                return False

    def _get_next(self) -> str|int:
        """
        Get Next Indexes Or Char From File
        """
        self._file.seek(self._current, 0)
        get = self._file.read(1)
        self._current += 1
        return get

    def __len__(self) -> int:
        """
        Length Of Indexes
        """
        # Check If is Binarray File Size Is Length
        if self._config['mode'].mode_type == self.PROTOCOL.MODETYPE.BIN:
            return self._end
        # If Text File Length Must Size Divided by '2' - 'unicode staff'
        return self._end // 2

    def __iter__(self) -> Iterator[int | str]:
        """
        Make Iterator
        """
        if self._file.closed:
            raise AccessDeniedFileIsClosed
        return super(BaseFileIndexes, self).__iter__()

    def __next__(self) -> int | str:
        """
        Next Indexes With Orderize by Wrapped Order
        """
        if self._file.closed:
            raise AccessDeniedFileIsClosed

        if self.ended():
            raise StopIteration

        size, skip, mode = self._config['size'], self._config['skip'], self._config['mode']

        temp = []
        count = 0

        while count < size:
            get = self._get_next()

            if isinstance(get, int):
                if bytes([get]) == skip:
                    continue
            elif isinstance(get, str):
                if get == skip:
                    continue

            temp.append(get)
            count += 1

        if len(temp) > 1:
            return self._inorder(self.PROTOCOL(self.joiner(temp, mode), mode), self.WRAPPED)
        else:
            return self._inorder(self.PROTOCOL(temp.pop(), mode), self.WRAPPED)

    @staticmethod
    def joiner(value: list[int | str], valid_mode: ModeName) -> str|int:
        """
        Static Method `joiner` join indexes value after Read if Need for joining To Gether For Validation
        args:
            value [list[int|str]]: [Read Temp].
            mode [str]: [File Mode].

        return:
            [str|int]: [Joined Value - Valid Indexes]
        """
        match valid_mode.mode_type:
            case ModeType.TXT:
                return ''.join(value)
            case ModeType.BIN:
                return b''.join([bytes([i]) for i in value])


# FILE PATH INDEXES
class FilePathIndexes(BaseFileIndexes):
    """
    Standard File Path Indexes - Work With FilePath & Mode
    """
    WRAPPED: Wrapped = Wrapped.INT
    PROTOCOL: ReadProtocol = ReadProtocol()

    def __init__(self, path: str | os.PathLike, mode: str = 'rb') -> None:
        """
        File Path Indexes - Instance of BaseFileIndexes
        Connect To Standard Read Protocol For Reading File Created by Standard Write Protocol
        const:
            WRAPPED [Wrapped]: [Standard Wrapper Types].
            PROTOCOL [ReadProtocol]: [Standard Read Protocol].

        args:
            path [str|PathLike]: [Indexes File Path].
            mode [str]: [Mode Opening File] default is 'rb'.
        """
        path = os.path.realpath(path)
        file_io = open(path, mode)
        super(FilePathIndexes, self).__init__(file_io)

        self.closed = self._file.closed

    def close(self) -> None:
        """
        Closing File - if Use `with` Statement Automatic Closing File After Done Working
        """
        self._file.close()
        self.closed = self._file.closed

    def __exit__(self, *_) -> None:
        """
        exit for with statement
        """
        try:
            pass
        finally:
            self.close()
            super(FilePathIndexes, self).__exit__()


# FILE OBJECT INDEXES
class FileObjectIndexes(BaseFileIndexes):
    """
    Standard File Object Indexes - Work With FileIO
    """
    WRAPPED: Wrapped = Wrapped.INT
    PROTOCOL: ReadProtocol = ReadProtocol()


# INDEXES
class Indexes(BaseIndexes):
    """
    Standard Indexes Object
    """
    WRAPPED: Wrapped = Wrapped.INT



__dir__ = ('T_INDEXES', 'BaseIndexes', 'BaseFileIndexes', 'Indexes', 'FileObjectIndexes', 'FilePathIndexes')
