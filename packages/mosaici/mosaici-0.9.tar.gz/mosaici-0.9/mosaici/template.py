from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
import os

# IMPORT LOCAL
from mosaici.exceptions import *
from mosaici.order import Order, BaseOrder
from mosaici.block import Block, BaseBlock
from mosaici.pattern import Convertor


# IMPORT TYPING
from typing import NamedTuple, Iterator

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

# DEFAULT BLOCK ITER TYPE SUPPORT
T_ITER = tuple[int, ...] | list[int]


# TEMPLATE ABSTRACT
class BaseTemplate:
    REPEAT: int
    SIZE: int
    ORDER: BaseOrder
    BLOCK: BaseBlock
    SEPARATOR: str
    DEFAULT_SYMBOL: tuple[str, ...]

    def __init__(
        self,
        blocks: tuple[BaseBlock, ...] = None,
        order: BaseOrder | str = None,
        default_block: BaseBlock | T_ITER = None,
        ) -> None:
        """
        const:
            REPEAT [int]: [Repeat Order Pattern if Use `Order` or `DefaultOrder`].
            SIZE [int]: [How Many Block in Template Only if Order is `None`].
            ORDER [BaseOrder]: [Order Object Must be instance of BaseOrder].
            BLOCK [BaseBlock]: [Block Object Must be instance of BaseBlock].
            SEPARATOR [str]: [Seperator Use For `Data to indexes` & `Indexes to Data`].
            DEFAULT_SYMBOL [tuple[str, ...]]: [Default Symbol When Want Use Default Order].
        args:
            blocks [tuple[BaseBlock]]: [Blocks if is `None` Make Blocks For Template] default is None.
            order [BaseOrder | str]: [Order for change layout Blocks & Template] default is None.
                ** order is None means without order pattern. **
                ** if want use default order use default symbol. **
            default_block [Block | T_ITER]: [Use Default Block for Making New Block Reletive With Default block] default is None.
        """

        if not self.REPEAT or not self.SIZE or not self.ORDER or not self.DEFAULT_SYMBOL:
            raise NotImplemented

        self._template = blocks
        self._default_block = default_block if default_block is not None else self.BLOCK(order=self.BLOCK.DEFAULT_SYMBOL[0])

        self._temp_block = None

        if isinstance(order, str) and order not in self.DEFAULT_SYMBOL:
            self._order = self.ORDER(order)
        else:
            self._order = order

        if isinstance(self._order, str) and self._order in self.DEFAULT_SYMBOL:
            self._order = self.default_order(self.ORDER, self.SIZE)

        if self._template is None:
            self._make_template()

        # Make This Object Iterable
        self._current = 0

    def _gen_default_block(self) -> BaseBlock:
        """
        Make Block When Order is None
        return:
            [BaseBlock]: [return new created block].
        """
        raise NotImplemented

    def _make_template(self) -> None:
        """
        Create Template
        """
        raise NotImplemented

    def to_hex(self) -> tuple[list[hex], ...]:
        """
        Template To Standard Mosaic Hex
        return:
            [tuple[list[hex]]]: [Tuple Of Hex Block]
        """
        return [i.to_hex() for i in self._template]

    def to_bytes(self) -> tuple[list[bytes], ...]:
        """
        Template to Bytes
        return:
            [tuple[list[bytes]]]: [Tuple Of Bytes Block]
        """
        return [i.to_bytes() for i in self._template]

    def to_bin(self) -> tuple[list[bin], ...]:
        """
        Template to Standard Mosaic Binarray Block
        return:
            [tuple[list[bin]]]: [Tuple Of Binarray Block]
        """
        return [i.to_bin() for i in self._template]

    def to_oct(self) -> tuple[list[oct], ...]:
        """
        Template to Standard Mosaic Octal Block
        return:
            [tuple[list[oct]]]: [Tuple Of Octal Block]
        """
        return [i.to_oct() for i in self._template]

    def index(self, block: int, value: int) -> int:
        """
        Index Value In Block
        args:
            block [int]: [Block Number]
            value [int]: [Value Target]
        return:
            [int]: [Indexes of Value in The Block]
        """
        block = self.valid_block(block, len(self))
        return self._template[block].index(value)

    def value(self, block: int, indexes: int) -> bytes:
        """
        Value From Indexes in Block
        args:
            block [int]: [Block Number].
            indexes [int]: [Index in Block].
        return:
            [bytes]: [Value in The Block & Indexes Place]
        """
        block = self.valid_block(block, len(self))
        return bytes([self._template[block][indexes]])

    def data_to_idx(self, data: bytes) -> str:
        """
        Data To Indexes
        args:
            data [bytes]: [Data For Convert To Indexes].
        return:
            [str]: [Indexes Of Data in Template].
        """
        res = []

        size = len(self)
        for idx_block, i in enumerate(data):
            _block = self.valid_block(idx_block, size)
            idx = self._template[_block].index(i)
            res.append(hex(idx).removeprefix('0x').upper())

        return self.SEPARATOR.join(res)

    def idx_to_data(self, indexes: str) -> bytes:
        """
        Indexes To Data
        args:
            indexes [str]: [Indexes Value].
        return:
            [bytes]: [Source Bytes].
        """
        indexes = indexes.split(self.SEPARATOR)
        res = b''

        size = len(self)
        for idx_block, i in enumerate(indexes):
            _block = self.valid_block(idx_block, size)
            value = self._template[_block][int(i, 16)]
            res += bytes([value])

        return res

    def save_template(self, path: str | os.PathLike) -> NamedTuple[int, int, int]:
        """
        Save Template Created For Use `Load` Saved Template Use Instance `BaseFileTemplate` Modules
        args:
            path [str|PathLike]: [File Path For Save Template]

        return:
            [NamedTuple[int, int, int]]: [Raw Bin Write, Block Count Write, Block Count Member]
            ** 'SaveInfo('write'= 65536, 'block'= 256, 'member'= 256)'
        """
        # Create Named Tuple For Return Saved
        _saved = NamedTuple('SavedInfo', (('write', int), ('block', int), ('member', int)))

        path = os.path.realpath(path)

        # Block Convert To Bytes
        to_bytes = (
            b''.join(block.to_bytes())
            for block in self
            )

        # Open File With Write Binarray Mode
        with open(path, 'wb') as f:
            saved_bin = f.write(b''.join(to_bytes))

        # Get Member Of Block - All Block Must Be Same Member
        _member = len(self._template[0])
        # Return SavedInfo - [Count Write Bin Into, Count Write Block, Count Block Member]
        return _saved(saved_bin, (saved_bin // _member), _member)

    def get_valid_block(self, block_idx: int) -> BaseBlock:
        """
        Get Valid Block
        Block Index Validate Before Getting Block.
        args:
            block_idx[int]: [Get Index Of Block].

        return:
            [BaseBlock]: [Block With Index].
        """
        # Validate Index Block With `valid_block()` Static Method.
        _block_idx = self.valid_block(block_idx, len(self))
        return self[_block_idx]

    def __iter__(self) -> Iterator[BaseBlock]:
        """
        Make Object Iterable
        """
        self._current = 0
        return self

    def __next__(self) -> BaseBlock:
        """
        Next Block
        """
        try:
            get = self._template[self._current]
            self._current += 1
            return get
        except IndexError:
            raise StopIteration

    def __enter__(self) -> object:
        return self

    def __len__(self) -> int:
        """
        Length Of Template
        """
        return len(self._template)

    def __getitem__(self, block_idx: int) -> BaseBlock:
        """
        Get Block From Indexes
        """
        return self._template[block_idx]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, BaseTemplate):
            return self._template == other._template
        raise NotImplementedError

    def __nq__(self, other: object) -> bool:
        if isinstance(other, BaseTemplate):
            return self._template != other._template
        raise NotImplementedError

    def __gt__(self, other: object) -> bool:
        if isinstance(other, BaseTemplate):
            return len(self) > len(other)
        raise NotImplementedError

    def __lt__(self, other: object) -> bool:
        if isinstance(other, BaseTemplate):
            return len(self) < len(other)
        raise NotImplementedError

    def __ge__(self, other: object) -> bool:
        if isinstance(other, BaseTemplate):
            return len(self) >= len(other)
        raise NotImplementedError

    def __le__(self, other: object) -> bool:
        if isinstance(other, BaseTemplate):
            return len(self) <= len(other)
        raise NotImplementedError

    def __contains__(self, value: int) -> bool:
        """
        All Blocks Must Be Same Value Only Value Places is Diffrent
        This Check if Value in First Block If True Means Value Existed In All Template Blocks
        args:
            value [int]: [Target Value].
        return:
            [bool]: [value contains template True OtherWise False]
        """
        return value in self[0]

    def __repr__(self) -> str:
        """
        Some Info With This Format
        'ObjectName(manyblocks, repeat, order)'
        """
        return f"{type(self).__qualname__}(blocks={len(self)}, repeat={self.REPEAT}, order={self._order})"

    def __str__(self) -> str:
        """
        Template To String With This Format - StringDict
        '{block_index: block, ...}'
        """
        to_str = (f"{n}: {str(i)}" for n,i in enumerate(self._template))
        return f"{{{', '.join(to_str)}}}"

    def __exit__(self, *_) -> None:
        try:
            pass
        finally:
            del self

    @staticmethod
    def default_order(order_obj: BaseOrder, size: int) -> BaseOrder:
        """
        Created Default Order
        args:
            order_object [BaseOrder]: [self.ORDER Use When This Method Calls]
            size [int]: [self.SIZE Use When This Method Calls] 
        """
        raise NotImplemented

    @staticmethod
    def valid_block(idx_block: int, size: int) -> int:
        """
        Validate Block Number From Template
        When Block Indexes Bigger Than Blocks Validate Block Number.
        args:
            idx_block [int]: [Number Of Block].
        return:
            [int]: [Block if Exists OtherWise Converted To Existed Block].
        """
        # I Changed Algorithm - Fixed Problem Maximum Recursion & Very Low Speed For Working
        while idx_block >= size:

            if idx_block == size:
                idx_block -= (size >> 1)
                continue

            elif idx_block <= (size + (size//2)):
                idx_block <<= 1
                continue

            elif idx_block >= (size * 2):
                idx_block //= size
                continue

            else:
                idx_block -= size
                continue

        return abs(idx_block)


# FILE TEMPLATE ABSTRACT
class BaseFileTemplate(BaseTemplate):
    SEPARATOR: str
    BLOCK: BaseBlock

    def __init__(self, path: str | os.PathLike, block_member: int = 256) -> None:
        """
        FileTemplate Load Saved Template.
        ** This Module Not Support Created Template Only For Loading And Use Saved Template.
        ** NOTE: For Copy Template Is Already Loaded Use `save_template()` module.
        const:
            SEPARATOR [str]: [Seperator Use For `Data to indexes` & `Indexes to Data`].
            BLOCK [BaseBlock]: [Block Object Must be instance of BaseBlock].

        args:
            path [str|PathLike]: [Path Saved Template File].
            block_member [int]: [Count Of Member In Blocks] default is `256`.

        ** NOTE: After Done Use This Module Must Be Closed File with `close()` method.
        ** NOTE: Use `with` Statement For Closing File Automatic After Done.
        """
        if not self.BLOCK or not self.SEPARATOR:
            raise NotImplementedError

        # Path To Real Path
        self._path = os.path.realpath(path)

        # Open Template File
        self._file = open(self._path, 'rb')
        self.closed = self._file.closed

        self._current= 0
        self._member = block_member

        self._end = self.size()

    @property
    def _template(self) -> tuple[BaseBlock]:
        """
        Property Get Template
        return:
            [tuple[BaseBlock]]:[All Block]

        ** example: 'tmpl = self._template'
        """
        return tuple(self)

    def close(self) -> None:
        """
        Close File
        if Use `with` Statement This Method Call Automatic After Done Working

        ** for check file is closed use Attr `closed`  [bool] if closed file `True` Otherwise `False`
        """
        self._file.close()
        self.closed = self._file.closed

    def size(self) -> int:
        """
        Size Of File.
        return:
            [int]: [Size Of File].
        """
        # Seeker Go End Of File
        self._file.seek(0,2)
        # Get Position Of Seeker
        get = self._file.tell()
        # Seeker Back To The Previous Position
        self._file.seek(self._current, 0)
        return get

    def value(self, block: int, indexes: int) -> bytes:
        """
        Get Value Of Indexes Order
        args:
            block [int]: [Block Index].
            indexes [int]: [Block Member].

        return:
            [bytes]: [Member from Block Placed in Index Order with indexes].
        """
        # Validate Block Index
        _block = self.valid_block(block, len(self))
        # Get Member
        get = self[_block][indexes]
        return bytes([get])

    def index(self, block: int, value: int) -> int:
        """
        Get Index Of Value
        args:
            block [int]: [Block Index].
            value [int]: [Value Place Index].

        return:
            [int]: [Index The Value In The Block].
        """
        # Validate Block
        _block = self.valid_block(block, len(self))
        # Get Index
        get = self[_block].index(value)
        return get

    def __len__(self) -> int:
        """
        Length Of Template
        return:
            [int]: [How Many Blocks In Template].
        """
        return self._end // self._member

    def __iter__(self) -> Iterator[BaseBlock]:
        """
        Iterator
        return:
            [object]: [Iterator File Template Object].
        """
        if self.closed:
            raise AccessDeniedFileIsClosed

        self._file.seek(0,0)
        return super(BaseFileTemplate, self).__iter__()

    def __next__(self) -> BaseBlock:
        """
        Next
        return:
            [BaseBlock]: [Next Block].
        """
        if self.closed:
            raise AccessDeniedFileIsClosed

        if self._current == self._end:
            raise StopIteration

        self._file.seek(self._current, 0)
        temp = self._file.read(self._member)
        self._current += self._member
        temp = tuple((int(i) for i in temp))
        return self.BLOCK(temp)

    def __getitem__(self, block_idx: int) -> BaseBlock:
        """
        Get Block With Block Idx
        """
        self._current = (block_idx * self._member)
        if self._current > (self._end - 256):
            self._current = 0
            raise IndexError
        return next(self)

    def __repr__(self) -> str:
        """
        Repr Method
        return:
            [str]: [Info From FileTemplate (`PATH`, `BLOCK`, `MEMBER`)]
        """
        return f"{type(self).__qualname__}(PATH: '{self._path}', BLOCK: {len(self)}, MEMBER: {self._member})"

    def __str__(self) -> str:
        """
        Template To String With This Format - StringDict
        '{block_index: block, ...}'
        """
        to_str = (f"{n}: {str(i)}" for n,i in enumerate(self))
        return f"{{{', '.join(to_str)}}}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, BaseTemplate):
            return all((it == ot for it, ot in zip(self, other)))
        raise NotImplementedError

    def __nq__(self, other: object) -> bool:
        if isinstance(other, BaseTemplate):
            return any((it != ot for it, ot in zip(self, other)))
        raise NotImplementedError

    def __exit__(self, *_) -> None:
        try:
            pass
        finally:
            self._file.close()
            del self


# TEMPLATE
class Template(BaseTemplate):
    """
    Template Module Instance of `BaseTemplate`
    Customize Method : `_gen_default_block`, `_make_template`, `default_order`
    """
    REPEAT: int = 1
    SIZE: int = 256
    ORDER: Order = Order
    BLOCK: Block = Block
    SEPARATOR: str = ' '
    DEFAULT_SYMBOL: tuple[str, ...] = ('', ' ', '/', '-', '#', '!')

    def _gen_default_block(self) -> Block:
        """
        Generate Default Block
        return:
            [Block]: [Generated Block].
        """
        # Create New Block With Default Algorithm
        make_new = [*self._temp_block[1: ], *self._temp_block[: 1]]
        # Assign Created Block To '_temp_block' Attr
        self._temp_block = self.BLOCK(order='', default_block=make_new)
        return self._temp_block

    def _make_template(self) -> None:
        """
        Create Template
        Generate Full Template With Ordered Or Default Algorithm Or ...
        """
        # Check If Order Valid For Generate Or Not
        if self._order is None:
            # Without Order Template Generate
            self._temp_block = self._default_block
            self._template = tuple((self._gen_default_block() for _ in range(0, self.SIZE)))
            return

        # Create Template With Order
        order = self._order
        self._temp_block = self.BLOCK(order=order, default_block=self._default_block)

        counter = 0
        template = []

        # Generate Template With Repeat Size
        while counter < self.REPEAT:

            # Create Blocks Loop
            for _ in range(0, len(self._order)):
                # Add Generated Block To `template` List
                template.append(self.BLOCK(order=self._order, default_block=self._temp_block))
                # Last Generated Template Assign To `_temp_block` Attr
                self._temp_block = template[-1]

            counter += 1

        self._template = tuple(template)
        # Remove `_temp_block` Free Memory
        del self._temp_block

    @staticmethod
    def default_order(order_obj: Order, size: int) -> Order:
        """
        Default Order Generated If Order Default Order For Use
        args:
            order_obj [Order]: [Order Object For Return Default Order].
            size [int]: [Order Size Needed For How Many Order Generated].
        """
        SEPARATOR = order_obj.SEPARATOR
        CONVERTOR = lambda x: Convertor.std_hex(x)
        res = (f"{CONVERTOR(i)}/{CONVERTOR(i*2)}" for i in range(1, (size + 1)))
        return order_obj(SEPARATOR.join(res))


# FILE TEMPLATE
class FileTemplate(BaseFileTemplate):
    """
    FileTemplate - Instance of BaseFileTemplate
    Use This Module For Load Saved Template
    """
    SEPARATOR: str = ' '
    BLOCK: Block = Block



__dir__ = ('T_ITER', 'BaseTemplate', 'BaseFileTemplate', 'Template', 'FileTemplate')
