from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
from functools import lru_cache
from enum import Enum

# IMPORT TYPING
from typing import Iterator

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

# WRAPPED TYPE
class Wrapped(Enum):
    """
    Wrapped [Standard Returner Type]
    INT : [Return Integer] '1', '256'                       [int]
    HEX : [Return Standard Hex] '00', 'FF'                  [str]
    BIN : [Return Standard Binarray] '00000000', '11111111' [str]
    OCT : [Return Standard Octal] '000', '377'              [str]
    --- See `Convertor` Object
    """
    INT = 'int'
    HEX = 'hex'
    BIN = 'bin'
    OCT = 'oct'

    @staticmethod
    def by_name(name: str) -> Wrapped:
        """
        args:
            name [str]: [Get Wrapped Type With Name]
                ** available names: [int], [hex], [bin], [oct] <<(Lower & Upper & ...) is Supports>>.
        return:
            [Wrapped] : [Valid Type With Name]
        """
        name = name.lower()
        names = {'int': Wrapped.INT, 'hex': Wrapped.HEX, 'bin': Wrapped.BIN, 'oct': Wrapped.OCT}

        if name not in names:
            raise NameError
        return names[name]


# STANDARD CONVERTOR
class Convertor:

    @staticmethod
    def int_to_order(value: int, order: Wrapped) -> int | str:
        """
        int Convert To Standard Ordered Value

        args:
            value [int]: [int Value] '0', '255'
            order [Wrapped]: [Standard Wrapped Type]

        return:
            [int | str]: [Standard Value Type Of Ordered]
        """
        match order.value:
            case 'int':
                return value

            case 'hex':
                return hex(value).removeprefix('0x').zfill(2).upper()

            case 'bin':
                return bin(value).removeprefix('0b').zfill(8)

            case 'oct':
                return oct(value).removeprefix('0o').zfill(3)

    @staticmethod
    def hex_to_order(value: str, order: Wrapped) -> int | str:
        """
        Standard Hex Convert To Standard Ordered Value

        args:
            value [str]: [Standard Hex Value] '00', 'FF'
            order [Wrapped]: [Standard Wrapped Type]

        return:
            [int | str]: [Standard Value Type Of Ordered]
        """
        match order.value:
            case 'hex':
                return value

            case 'int':
                return int(value, 16)

            case 'bin':
                return bin(int(value, 16)).removeprefix('0b').zfill(8)

            case 'oct':
                return oct(int(value, 16)).removeprefix('0o').zfill(3)

    @staticmethod
    def std_hex(value: int | str) -> hex:
        """
        Value To Standard `HEX`
        Length Of Standard Hex: 2
        args:
            value [int | str]: [Value Must be int Or Standard String]

        return:
            [hex]: [Standard `Hex` Value]
        """
        validator = lambda x: hex(x).removeprefix('0x').upper().zfill(2).upper()

        if isinstance(value, int):
            return validator(value)

        else:
            match len(value):
                case 2:
                    # Standard Hex -> '00': '00', 'FF': 'FF'
                    return value
                case 3:
                    # Standard Octal To Hex -> '000': '00', '377': 'FF'
                    return validator(int(value, 8))
                case 8:
                    # Standard Binarray To Hex -> '00000000': '00', '11111111': 'FF'
                    return validator(int(value, 2))

    @staticmethod
    def std_int(value: int | str) -> int:
        """
        Value To `int`
        args:
            value [int | str]: [Value Must be int Or Standard String]

        return:
            [int]: [`int` Value]
        """
        if isinstance(value, int):
            return value

        else:
            match len(value):
                case 2:
                    # Standard Hex To int -> '00': '0', 'FF': '255'
                    return int(value, 16)
                case 3:
                    # Standard Octal To int -> '000': '0', '377': '255'
                    return int(value, 8)
                case 8:
                    # Standard Binarray To int -> '00000000': '0', '11111111': '255'
                    return int(value, 2)

    @staticmethod
    def std_oct(value: int | str) -> oct:
        """
        Value To Standard `Octal`
        Length Of Standard Octal: 3
        args:
            value [int | str]: [Value Must be int Or Standard String]

        return:
            [oct]: [Standard `Octal` Value]
        """
        validator = lambda x: oct(x).removeprefix('0o').zfill(3)
        if isinstance(value, int):
            return validator(value)

        else:
            match len(value):
                case 2:
                    # Standard Hex To Oct -> '00': '000', 'FF': '377'
                    return validator(int(value, 16))
                case 3:
                    # Standard Octal -> '000': '000', '377': '377'
                    return value
                case 8:
                    # Standard Binarray To int -> '00000000': '000', '11111111': '377'
                    return validator(int(value, 2))

    @staticmethod
    def std_bin(value: int | str) -> bin:
        """
        Value To Standard `Binarray`
        Length Of Standard Binarray: 8
        args:
            value [int | str]: [Value Must be int Or Standard String]

        return:
            [bin]: [Standard `Binarray` Value]
        """
        validator = lambda x: bin(x).removeprefix('0b').zfill(8)
        if isinstance(value, int):
            return validator(value)

        else:
            match len(value):
                case 2:
                    # Standard Hex To Binarray -> '00': '00000000', 'FF': '11111111'
                    return validator(int(value, 16))
                case 3:
                    # Standard Octal To Binarray -> '000': '00000000', '377': '11111111'
                    return validator(int(value, 8))
                case 8:
                    # Standard Binarray -> '00000000': '00000000', '11111111': '11111111'
                    return value


# PATTERN ABSTRACT
class BasePattern:
    WRAPPED: Wrapped

    def __init__(self) -> None:
        """
        const:
            WRAPPED [Wrapped]: [Standard Wrapper Types]
        """
        if not self.WRAPPED:
            raise NotImplementedError

        self._current = 0

    def __len__(self) -> int:
        """
        Length Of Value
        """
        raise NotImplemented

    def __iter__(self) -> Iterator[int | str]:
        """
        Iterator
        """
        self._current = 0
        return self

    def __next__(self) -> int | str:
        """
        Next Value
        """
        raise NotImplemented

    def __enter__(self) -> object:
        return self

    def __exit__(self, *_) -> None:
        try:
            pass
        finally:
            del self

    @staticmethod
    @lru_cache(256)
    def _inorder(value: int | str, order: Wrapped) -> int | str:
        """
        Convert Standard Hex To Order
        """
        if isinstance(value, int):
            return Convertor.int_to_order(value, order)
        else:
            return Convertor.hex_to_order(value, order)



__dir__ = ('Wrapped', 'Convertor', 'BasePattern')
