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
from mosaici.app.tools import Json
from mosaici.app.mosaici_actions import make_template_from_orders

# IMPORT TYPING
from typing import Final

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

class ThePath:
    USER: Final = os.path.expanduser('~')
    MOSAICI: Final = os.path.realpath(os.path.join(USER, 'mosaici/'))
    CONFIG: Final = os.path.realpath(os.path.join(MOSAICI, 'conf.json'))


def is_first_run() -> bool:
    if os.path.isdir(ThePath.MOSAICI):
        return False
    return True

def make_conf(conf_path: str, templates_dir: str, order_store_path: str) -> None:
    conf = {
        "default_paths": {"templates_dir": templates_dir,"order_store": order_store_path},

        "app": {"template_call": "('template', '*tt')", "manage_call": "('manage', '*ma')"},

        "template_app_default":{
        "repeat": 1,
        "order": None,
        "string": None,
        "size": 256,
        "length": None,
        "replace": False,
        "saveorder": False
        },

        "mosaici_app_default":{
        "template": "default.tt",
        "mode": "mosaic",
        "startblock": 0
        }
    }

    Json.save(conf, conf_path)

def make_order(order_store_path: str) -> None:
    default_od = [
    'B1/EF', 'D2/D3', '3D/B9', 'AD/CA', '44/D9', '55/B0',
    '5B/6A', 'B9/BE', '54/71', '52/CC', '6B/AD', '2F/CB',
    'B0/D0', 'C9/DF', '4E/A7', 'B7/D5', '26/BF', 'A7/C4',
    'A7/C1', '5E/C4', 'BD/CE', '77/EC', 'DB/F0', 'C7/D4',
    '30/D3', 'D1/E2', 'AC/DE', '68/7B', '4D/C8', '33/BB',
    '52/D7', '37/4B', '5F/D4', '47/C9', '50/50', '47/C9',
    '5F/D4', '37/4B', '52/D7', '33/BB', '4D/C8', '68/7B',
    'AC/DE', 'D1/E2', '30/D3', 'C7/D4', 'DB/F0', '77/EC',
    'BD/CE', '5E/C4', 'A7/C1', 'A7/C4', '26/BF', 'B7/D5',
    '4E/A7', 'C9/DF', 'B0/D0', '2F/CB', '6B/AD', '52/CC',
    '54/71', 'B9/BE', '5B/6A', '55/B0', '44/D9', 'AD/CA',
    '3D/B9', 'D2/D3','B1/EF'
    ]

    order_store = {
        "default.tt": {
            "order": " ".join(default_od),
            "repeat": 2,
        }
    }

    Json.save(order_store, order_store_path)

def first_run_conf() -> int:
    rp = os.path.realpath
    data = rp(os.path.join(ThePath.MOSAICI, 'data'))
    templates = rp(os.path.join(data, 'templates'))

    conf = rp(os.path.join(ThePath.MOSAICI, 'conf.json'))
    orders = rp(os.path.join(data, 'orders.json'))

    os.makedirs(templates)
    make_order(orders)
    make_conf(conf, templates, orders)

    mk_tmpl = [*make_template_from_orders(orders, templates)]

def main() -> int:
    if is_first_run():
        return first_run_conf()

    return 0



__dir__ = ("ThePath", "is_first_run", "make_conf", "make_order", "first_run_conf", "main")


if __name__ == "__main__":
    raise SystemExit(main())
