from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
from io import FileIO

# IMPORT LOCAL
from mosaici.exceptions import *
from mosaici.pattern import Wrapped, BasePattern
from mosaici.protocol import BaseProtocol, WriteProtocol, ModeName

# IMPORT TYPING
from typing import Iterator, Iterable, Callable, Generator

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

# STORE INDEXES ABSTRACT
class BaseStoreIndexes(BasePattern):

    def __init__(self, indexes: Iterable[int] | None = None) -> None:
        """
        Store Indexes - Instance of BasePattern.
        Support `with` Statement.

        const:
            WRAPPED [Wrapped]: [Standard Wrapper Types].

        args:
            indexes [Iterable[int]|None]: [Setup Indexes Value] default is None.
            ** Get Indexes Use `indexes` property or `get_indexes` methods.
            ** Can Set Or Change After With Use `indexes` property or `set_indexes` methods.

        ** example `set, get` indexes:
                # Initialize
                store = StoreIndexes()

                # Property Set
                store.indexes = indexes_value

                # Property Get
                get = store.indexes

                # Method - Set
                store.set_indexes(indexes_value)

                # Method - Get
                get = store.get_indexes()

        ** change or update indexes with use set property or set method.
        """
        super(BaseStoreIndexes, self).__init__()

        self._indexes: Iterable[int] = indexes

    @property
    def indexes(self) -> Iterable[int]:
        """
        Get Indexes - Property
        """
        if self._indexes is None:
            raise IndexesIsNotDefinedError

        return self._indexes

    @indexes.setter
    def indexes(self, indexes: Iterable[int]) -> None:
        """
        Set Indexes - Property
        """
        self._indexes = indexes

    def get_indexes(self) -> Iterable[int]:
        """
        Get Indexes Functional
        """
        if self._indexes is None:
            raise IndexesIsNotDefinedError

        return self._indexes

    def set_indexes(self, indexes: Iterable[int]) -> None:
        """
        Set Indexes Functional
        """
        self._indexes = indexes

    def __len__(self) -> int:
        """
        Len of Indexes

        ** if indexes instance of Generator is Exclusive
        """
        if self._indexes is None:
            raise IndexesIsNotDefinedError

        if isinstance(self._indexes, (list, tuple)):
            return len(self._indexes)

        self._indexes = tuple(self._indexes)
        return len(self._indexes)

    def __next__(self) -> int | str:
        if self._indexes is None:
            raise IndexesIsNotDefinedError

        if isinstance(self._indexes, (list, tuple)):
            try:
                get = self._indexes[self._current]
                self._current += 1
                return self._inorder(get, self.WRAPPED)
            except IndexError:
                raise StopIteration

        elif isinstance(self._indexes, (Iterator, Iterable, Generator)):
            try:
                get = next(self._indexes)
                self._current += 1
                return self._inorder(get, self.WRAPPED)

            except StopIteration:
                self._indexes = None
                raise StopIteration

            except Exception as err:
                raise err

    def __str__(self) -> str:
        if self._indexes is None:
            return f'{type(self).__qualname__}(None)'

        to_str = lambda x: x if isinstance(x, str) else str(x)

        if isinstance(self._indexes, (list, tuple)):
            return f'{type(self).__qualname__}({"".join((to_str(i) for i in self._indexes))})'

        self._indexes = tuple(self._indexes)
        return f'{type(self).__qualname__}({"".join((to_str(i) for i in self._indexes))})'

    def __repr__(self) -> str:
        if self._indexes is None:
            return f'{type(self).__qualname__}([None])'
        return f'{type(self).__qualname__}([TYPE: {type(self._indexes).__qualname__}])'

    def __exit__(self, *_) -> None:
        try:
            pass
        finally:
            del self._indexes
            super(BaseStoreIndexes, self).__exit__()


# STORE TO OBJECT ABSTRACT
class BaseStoreObject(BaseStoreIndexes):

    def _validate(self) -> tuple[int | str, ...]:
        """
        Validate Indexes To Indexable Object.
        return:
            [tuple[int|str, ...]: [Index Ordered].
        """
        if self._indexes is None:
            raise IndexesIsNotDefinedError

        if isinstance(self._indexes, (list, tuple)):
            return tuple((self._inorder(i, self.WRAPPED) for i in self._indexes))

        self._indexes = tuple(self._indexes)
        return tuple((self._inorder(i, self.WRAPPED) for i in self._indexes))

    def join_byte(self, separator: bytes = b'') -> bytes:
        """
        Convert to Bytes and Join to gether.
        args:
            separator [bytes]: [Separator for Joining bytes] default is b''.

        return:
            [bytes]: [Join All indexes Sequence Of Bytes].
        """
        to_byte = lambda x: bytes([x]) if isinstance(x, int) else bytes([self._inorder(x, Wrapped.INT)])
        return separator.join((to_byte(i) for i in self._validate()))

    def join_str(self, separator: str = '') -> str:
        """
        Convert to String and Join together.
        args:
            separator [str]: [Separator for Joining bytes] default is ''.

        return:
            [str]: [Join All indexes Sequence Of str].
        """
        to_str = lambda x: x if isinstance(x, str) else str(x)
        return separator.join((to_str(i) for i in self._validate()))

    def to_tuple(self) -> tuple[str | int, ...]:
        """
        Indexes To tuple Of Ordered in `Wrapped`.
        return:
            [tuple[str|int, ...]]: [tuple of ordered].
        """
        return self._validate()

    def to_list(self) -> list[int | str]:
        """
        Indexes To list Of Ordered in `Wrapped`.
        return:
            [list[int|str, ...]]: [list of ordered].
        """
        return [*self._validate()]

    def to_dict(self, key: Callable = None) -> dict[int, int | str]:
        """
        Indexes To dict Of Ordered in `Wrapped`.
        args:
            key [Callable]: [Callable Object For Make Key From `int of value from indexes` and 'index of value'] default is None.

            ** key Call:
                key(value, index)

            ** key is None:
                Create Key First Is Standard Hex Value Second Index Of Value in Indexes Place.
                Pattern : {'00_0': '00', '01_1': '01'} -> {'HEX_INDEX': 'VALUE'}.

        return:
            [tuple[str|int, ...]]: [tuple of ordered].
        """

        if key is None:
            # Create Key First Is Standard Hex Value Second Index Of Value in Indexes Place
            # Pattern : {'00_0': '00', '01_1': '01'} -> {'HEX_INDEX': 'VALUE'}
            key = lambda x, i: f"{self._inorder(x, Wrapped.HEX)}_{i}"

        return {key(self._inorder(v, Wrapped.INT), i): v for i, v in enumerate(self._validate())}

    def to_set(self) -> set[int | str]:
        """
        Indexes To set Of Ordered in `Wrapped`.
        NOTE: Set Is Sorted Value.
        return:
            [set[int|str, ...]]: [set of ordered].
        """
        return set(self._validate())


# STORE FILE ABSTRACT
class BaseStoreFile(BaseStoreIndexes):
    PROTOCOL: BaseProtocol

    def __init__(self, indexes: Iterable[int] | None = None) -> None:
        """
        Store File - Instance of `BaseStoreIndexes`
        Support `with` Statement.

        const:
            PROTOCOL [BaseProtocol]: [Protocol For Writing Value].

        args:
            indexes [Iterable[int]]: [Indexes Value] Default is None.
        """
        if not self.PROTOCOL:
            raise NotImplementedError

        super(BaseStoreFile, self).__init__(indexes)
        self.mode_name = ModeName

    def write(self, file_obj: FileIO, truncate: bool = False) -> int:
        """
        Indexes Write To File With Protocol

        args:
            file_obj [FileIO]: [File Object Object With `write` Method].
                ** Support File Mode See `ModeName` Object.
            truncate [bool]: [Truncate File] default is `False`.

        
        ** example:
            # This Example We Use `with` Statement

            with StoreFile(indexes) as store:
                # Text
                with open(file, 'w') as f:
                    # Write To Text File With Text Protocol - See Protocol
                    store.write(f)

                # Change Indexes To New Indexes Value
                store.indexes = other_indexes
                
                # Binarray
                with open(other_file, 'wb') as f:
                    # Write To Binarray File With Byte Protocol - See Protocol
                    store.write(f)
        """
        if not file_obj.writable():
            raise FileIsNotWritableError

        if truncate:
            file_obj.truncate()

        mode = self.mode_name(file_obj.mode)

        tokenize = (self.PROTOCOL(i, mode) for i in self)
        return file_obj.write(self.PROTOCOL[mode].join(tokenize))

    def write_raw(self, file_obj: FileIO, truncate: bool = False) -> int:
        """
        Indexes Write To File Without Protocol

        args:
            file_obj [FileIO]: [File Object Object With `write` Method].
                ** Support File Mode See `ModeName` Object.
            truncate [bool]: [Truncate File] default is `False`.
        """
        if not file_obj.writable():
            raise FileIsNotWritableError

        if truncate:
            file_obj.truncate()

        mode = self.mode_name(file_obj.mode)

        count = 0
        match mode.mode_type:
            case self.PROTOCOL.MODETYPE.TXT:
                for i in self:
                    if isinstance(i, str):
                        count += file_obj.write(i)
                    else:
                        count += file_obj.write(str(i))
            case self.PROTOCOL.MODETYPE.BIN:
                for i in self:
                    if isinstance(i, int):
                        count += file_obj.write(bytes([i]))
                    else:
                        count += file_obj.write(i.encode('ascii'))
        return count

# STORE INDEXES TO FILE
class StoreFileIndexes(BaseStoreFile):
    """
    Standard Store File Indexes Instance Of `BaseStoreFile`
    """
    WRAPPED: Wrapped = Wrapped.INT
    PROTOCOL: BaseProtocol = WriteProtocol()


# STORE INDEXES TO OBJECT
class StoreObjectIndexes(BaseStoreObject):
    """
    Standard Store Object Indexes Instance Of `BaseStoreObject`
    """
    WRAPPED: Wrapped = Wrapped.INT


__dir__ = ('BaseStoreIndexes', 'BaseStoreFile', 'BaseStoreObject', 'StoreFileIndexes', 'StoreObjectIndexes')
