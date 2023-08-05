from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT TYPING
from typing import Generator, Iterable, Iterator

# IMPORT LOCAL
from mosaici.pattern import Convertor

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

# ORDER ABSTRACT
class BaseOrder:
    SEPARATOR: str
    MIXER: str

    def __init__(self, order: str, limited: bool = False) -> None:
        """
        const:
            SEPARATOR [str]: [Separator Symbol Between Pattern]
            MIXER [str]: [Symbol Mixer Starts & Ends Pattern]
        args:
            order [str]: [Order Sequence].
            limited [bool]: [Limited Order If Not Limited Wrapped EndLess] default is `True`.
        """
        if not self.SEPARATOR or not self.MIXER:
            raise NotImplementedError

        self._order = order.split(self.SEPARATOR)
        self._current = 0
        self._limited = limited

    def endless(self) -> bool:
        """
        return:
            [bool]: [if limited is `False` means `Endless` is `True`].
            ** not limited **
        """
        return not self._limited

    def orderize(self) -> None:
        """
        Change Pattern When Not Limited (endless)
        """
        raise NotImplemented

    def __iter__(self) -> Iterator[tuple[int, int]]:
        # Reset Current Position Index To Start
        self._current = 0
        return self

    def __enter__(self) -> object:
        return self

    def __next__(self) -> tuple[int, int]:
        """
        Return Tuple (Start, End) Integer Value
        """
        # EndLess Iter
        if self._current >= len(self._order) and not self._limited:
            self.orderize()
            self._current = 0

        try:
            start, end = self._order[self._current].split(self.MIXER)
            self._current += 1
            return int(start, 16), int(end, 16)
        except IndexError:
            raise StopIteration

    def __eq__(self, other: object) -> bool:
        if isinstance(other, BaseOrder):
            return self._order == other._order
        raise NotImplementedError

    def __nq__(self, other: object) -> bool:
        if isinstance(other, BaseOrder):
            return self._order != other._order
        raise NotImplementedError

    def __exit__(self, *_) -> None:
        try:
            pass
        finally:
            del self

    def __repr__(self) -> str:
        """
        Repr Of Order
        """
        order = (i.split(self.MIXER) for i in self._order)
        order = (f'[{int(start, 16)}:{int(end, 16)}]' for start, end in order)
        mode = 'Limited' if self._limited else 'EndLess'
        return f"{type(self).__qualname__}({mode}, ({', '.join(order)}))"

    def __str__(self) -> str:
        """
        Order To String
        """
        return f"{type(self).__qualname__}({', '.join(self._order)})"

    def __len__(self) -> int:
        """
        Len Order
        """
        return len(self._order)

    @staticmethod
    def from_string(
        inp: str | Iterable[str],
        length: int = None,
        separator: str = ' ',
        mixer: str = '/',
        ) -> str:
        """
        FROM STRING `Static Method` - SUPPORT UNICODE CHARACTER
        This Method Calls Function `order_from_string()`
        args:
            inp [str | Iterable[str]]: [String Input For Wrapping Order Pattern String].
            length [int]: [Order Length] default is `None`:
                ** `None` Means Length Of String
            separator [str]: [Separator Symbol Between Pattern] default is `' '`.
            mixer [str]: [Symbol Mixer Starts & Ends Pattern] default is `'/'`.

        return:
            [str]: [Order Support String Pattern].
        """
        return order_from_string(inp, length, separator, mixer)


# ORDER
class Order(BaseOrder):
    """
    Order Object Instance Of BaseOrder
    """
    SEPARATOR = ' '
    MIXER = '/'

    def orderize(self) -> None:
        """
        Change Pattern With Standard Formolla
        """
        self._order = [*self._order[len(self._order)//2:], *self._order[: len(self._order)//2]]


# MAKE ORDER FROM STRING
def order_from_string(
    inp: str | Iterable[str],
    length: int = None,
    separator: str = ' ',
    mixer: str = '/',
    ) -> str:

    """
    ORDER FROM STRING - SUPPORT UNICODE CHARACTER
    args:
        inp [str | Iterable[str]]: [String Input For Wrapping Order Pattern String].
        length [int]: [Order Length] default is `None`:
            ** `None` Means Length Of String
        separator [str]: [Separator Symbol Between Pattern] default is `' '`.
        mixer [str]: [Symbol Mixer Starts & Ends Pattern] default is `'/'`.

    return:
        [str]: [Order Support String Pattern].
    """

    def generate(string: str | Iterable[str], end: int) -> Generator[int, None, None]:
        """
        Generate String Char One by One
        args:
            string [str | Iterable[str]]: [Input for Wrapping].
            end [int]: [Length Of Generate Limited].

        return:
            [Generator[int, None, None]]: [Yield ord of char].
        """
        # Make Subscriptable input
        dec = [*string]

        size = len(dec)
        idx = 0
        count = 0

        while count < end:

            # Check if index End Of String Make New Pattern
            if idx >= len(dec):
                dec = [*dec[size//2:], *dec[: size//2]]
                idx = 0

            yield ord(dec[idx])

            idx += 1
            count += 1

    def validrange(inp: int) -> int:
        """
        Validate Range Of Input
        Range For Order Support `0`, `255` - Bytes Range Support
        args:
            inp [int]: [Wrapped Value From Generator].

        return:
            [int]: [Intiger Validate Range].
        """
        while inp > 255:
            if inp >= 2048:
                inp >>= 2
            else:
                inp -= (16 + inp // 4)

        return inp

    length = length if length is not None else len(inp)

    # Active Wrapped - `generate()` inner Function
    # -- Start Value Active - input is inp
    wrapped_start = generate(inp, length)
    # -- End Value Active - input is reversed inp
    wrapped_end = generate(reversed(inp), length)

    # Validate Place Of Value
    place = lambda x, y: (x, y) if x <= y else (y, x)

    # Convert To Valid Pattern Order
    # -- Make Standard Hex Value For Starts & Ends Order Then Joined With `mixer` Symbol
    con = lambda x, y: f"{Convertor.std_hex(x)}{mixer}{Convertor.std_hex(y)}"

    # Make Pattern Order
    pack = (
        con(*place(validrange(start), validrange(end)))
        for start, end in zip(wrapped_start, wrapped_end)
    )

    # Joining & Return Pattern
    return separator.join(pack)



__dir__ = ('BaseOrder', 'Order', 'order_from_string')
