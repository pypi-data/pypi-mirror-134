from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
import os

from typing import Literal, Generator

# IMPORT MOSAICI
from mosaici.order import order_from_string
from mosaici.template import Template
from mosaici.pattern import Wrapped
from mosaici.indexpack import Indexes
from mosaici.mosaic import MosaicFile
from mosaici.store import StoreFileIndexes

# IMPORT APP
from mosaici.app.tools import Json, path_join

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

# MAKE TEMPLATE - USE `TEMPLATE MODULE`
def make_template(repeat: int, size: int, order: str, path: str, replace: bool) -> tuple:
    # Make Template HighLevel Function
    if os.path.isfile(path) and not replace:
        raise FileExistsError("Use `--replace` Option Overriding Existed File")

    cls_template = Template
    cls_template.REPEAT = repeat
    cls_template.SIZE = size

    # Template Generating Initialize
    with cls_template(order=order) as cl_tmp:
        # Saving Generated Template
        res = cl_tmp.save_template(path)

    return res

# ORDER FROM STRING
def from_string(string: str, length: int, separator: str = ' ', mixer: str = '/') -> str:
    return order_from_string(string, length, separator, mixer)

# MOSAIC FILE HIGH LEVEL FUNCTION
def mosaic_file(
    template: Template | tuple[str, int],
    data_or_path: bytes | str | Indexes,
    res_path: str | os.PathLike = None,
    start_block: int = 0,
    type: Literal['data', 'indexes'] = 'data',
    ) -> tuple | bytes | Indexes:
    type = type.lower()
    is_file = True if isinstance(data_or_path, str) else False

    if is_file:
        data_or_path = os.path.realpath(data_or_path)
        if res_path is None:
            raise ValueError

    if type not in ('data', 'indexes'):
        raise NameError

    with MosaicFile(template, active_maker=False) as ms:
        if is_file:
            if type == 'data':
                return ms.to_mosaici(data_or_path, res_path, start_block, "wb", True)
            elif type == 'indexes':
                return ms.to_data(data_or_path, res_path, start_block, 'rb')
        else:
            idx = Indexes

            if type == 'data':
                temp = ms.data_to_idx(data_or_path, start_block)
                if res_path is None:
                    idx.WRAPPED = Wrapped.HEX
                    temp = idx([*temp])
                    return temp
                else:
                    with StoreFileIndexes(temp) as st:
                        with open(res_path, 'wb') as res:
                            return st.write(res, True)

            elif type == 'indexes':

                if not isinstance(data_or_path, Indexes):
                    idx.WRAPPED = Wrapped.INT
                    data_or_path = idx(data_or_path)

                temp = ms.idx_to_data(data_or_path, start_block)

                if res_path is not None:

                    with open(res_path, 'wb') as res:
                        return res.write(b''.join(temp))

                return b''.join(temp)

# MAKE TEMPLATES FROM ORDERS HIGH LEVEL FUNCTION
def make_template_from_orders(path: str | os.PathLike, dirpath: str | os.PathLike) -> Generator[tuple[int, str, tuple], None, None]:
    path = os.path.realpath(path)
    dirpath = os.path.realpath(dirpath)
    load_file = Json.load(path)
    length = len(load_file)
    make = Template

    for tp, tv in load_file.items():
        _template_path = path_join(dirpath, tp)

        make.REPEAT = tv['repeat']
        # YIELD length of items in load file [int] & Name [str] & Result Save Templates [NamedTuple]
        yield length, tp, make(order= tv['order']).save_template(_template_path)



__dir__ = ('make_template', 'from_string', 'mosaic_file', 'make_template_from_orders')
