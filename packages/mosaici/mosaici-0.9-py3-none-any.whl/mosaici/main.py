from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
import os
import sys
import argparse

from typing import Sequence, Final

# IMPORT APP
from mosaici.app import mosaici_actions as m_act
from mosaici.app.tools import color_print as cprint
from mosaici.app.tools import Json, path_join, basename, center, monotonic, spacer, error

from mosaici.app import first_run


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

VERSION: Final = '0.9.1'

if first_run.is_first_run():
    cprint(center("... < Mosaici App is First Run > ..."), "title")
    cprint("/> Configure Requirements ", "work")
    t0 = monotonic()
    first_run.main()
    t1 = monotonic()
    cprint("~> Mosaici App is Configured", "result")
    cprint(f"!> TIME: {t1 - t0:.3f}", 'time')

CONFIG_PATH: Final = first_run.ThePath.CONFIG
CONFIG = Json.load(CONFIG_PATH)

def is_name(inp: str) -> bool:
    if '/' in inp:
        return False

    elif '\\' in inp:
        return False

    return True

def manage(parse: argparse.ArgumentParser) -> int:
    # Only For Passing App Mode Not Use Any Where
    parse.add_argument('mode')

    temp_dir_path = os.path.realpath(CONFIG['default_paths']["templates_dir"])

    parse.add_argument(
        '--makefromfile',
        nargs=2,
        type=str,
        default = None,
        help="Need 2 Value First `path_file` Second `directory` For Created Templates Saved Those Dir `Space String `' '` Mean Use Default templates Dir Path`"
    )

    parse.add_argument(
        '--updateconf',
        type=str,
        default= None,
        help="Path new Config File For Updating Config File"
    )

    parse.add_argument(
        '--conf',
        action = 'store_true',
        default= None,
        help="Get Config File Path"
    )

    parse.add_argument(
        '--templates',
        action = 'store_true',
        default= None,
        help="Get Templates Default Path"
    )

    parse.add_argument(
        '--templatelist',
        action = 'store_true',
        default= None,
        help="Get All Templates Name Existed in Templates Default Dir"
    )

    parse.add_argument(
        '--resetconf',
        action = 'store_true',
        default= False,
        help="Reset Config File To Default"
    )

    parse.add_argument(
        '--resettemplates',
        action = 'store_true',
        default = False,
        help="Reset Templates Remove All Templates & Make Default Template Only"
    )

    arguments = {**vars(parse.parse_args())}

    _space = spacer('-', None, 0)

    cprint(_space)
    cprint(center('<<< MOSAICI APP :: Manage >>>'), 'title')

    error_happen = False
    t0 = monotonic()

    # Get Config File Path
    if arguments['conf']:
        cprint("/> Get Config File Path", 'work')
        cprint(f"~> ConfAddress: {CONFIG_PATH}", 'result')

    # Get Templates Directory Path
    if arguments['templates']:
        cprint("/> Get Templates Dire Path", 'work')
        cprint(f"~> TemplatesAddress: {temp_dir_path}", 'result')

    # Get List Of Template Exists in Templates Directory
    if arguments['templatelist']:
        cprint("/> Templates Exists Name", 'work')
        lst = sorted(os.listdir(temp_dir_path))
        count = len(lst)
        empty = center('------', ' ', 5, 10)
        for num, temp in enumerate(lst, 1):
            size = os.path.getsize(path_join(temp_dir_path, temp))
            cprint(f'~> {num}/{count}:\t{temp}{empty}Size: {size}', 'result')

    # Make Templates From Orders File
    if arguments['makefromfile']:
        cprint("/> Make Templates From Orders File", 'work')
        order_file, dir_path = arguments['makefromfile']
        if dir_path.strip() == '':
            dir_path = temp_dir_path

        try:

            cprint("/> Initialize Maker", 'work')

            maker = m_act.make_template_from_orders(order_file, dir_path)

            cprint("/> Start Generating Template", 'work')

            empty = center('------', ' ', 5, 10)
            for idx, it in enumerate(maker, 1):
                count, name, make = it
                mk = f"WRITE: {make[0]} \t BLOCKS: {make[1]} \t MEMBERS: {make[2]}"
                cprint(f"~> {idx}/{count}: {name} {empty} {mk}", 'result')

        except Exception as err:
            error_happen = True
            err = error(err)
            cprint(err)

    # Update Config File With Other Config File
    if arguments['updateconf']:
        cprint("/> Update Config File", 'work')

        conf_path = CONFIG_PATH
        update_path = os.path.realpath(arguments['updateconf'])

        try:

            cprint("/> Load Updates File", 'work')

            update_value = Json.load(update_path)

            cprint("/> Updating Config File", 'work')

            Json.update(update_value, conf_path)

            cprint("~> Config is Updated", 'result')

        except Exception as err:
            error_happen = True
            err = error(err)
            cprint(err)

    # Reset Config File To Default
    if arguments['resetconf']:
        cprint("/> Reset Config File To Default", 'work')
        first_run.make_conf(
            CONFIG_PATH,
            CONFIG['default_paths']["templates_dir"],
            CONFIG['default_paths']["order_store"],
            )
        cprint("~> Config File is Reset", 'result')

    # Reset Templates To Default
    if arguments['resettemplates']:
        cprint("/> Reset Templates", 'work')
        order_store_path = CONFIG['default_paths']["order_store"]
        lst = os.listdir(temp_dir_path)
        lst = [os.path.realpath(path_join(temp_dir_path, i)) for i in lst]

        cprint("/> Removing All Templates", 'work')
        for temp in lst:
            os.remove(temp)
            cprint(f"~> [{basename(temp)}] is Removed", 'result')

        cprint(f"/> Reset Order Store", 'work')
        first_run.make_order(order_store_path)
        cprint(f"~> Order Store is Reset To Default", 'result')
        cprint(f"/> Make Default Template", 'work')
        mk = m_act.make_template_from_orders(order_store_path, temp_dir_path)
        for template in mk:
            cprint(f"~> {template[1]} is Created", "result")

    t1 = monotonic()

    cprint(f"!> TIME: {t1 - t0:.3f}", 'time')
    if error_happen:
        cprint(f"</ !! Manager Working is Problem Check Arguments And `TryAgain` !! />", 'warning')
    else:
        cprint(f"</ Manager Working is Done />", 'done')

    cprint(_space)
    return 0

def templates_app(parse: argparse.ArgumentParser) -> int:
    # Only For Passing App Mode Not Use Any Where
    parse.add_argument('mode')

    defaults = CONFIG['template_app_default']
    templates_dir = CONFIG['default_paths']["templates_dir"]
    order_store = CONFIG['default_paths']['order_store']

    parse.add_argument(
        'file',
        type=str,
        help="Path File For Saving Generated Template"
    )

    parse.add_argument(
        '--replace',
        action='store_true'  if not defaults['replace'] is True else 'store_false',
        default= defaults['replace'],
        help="File Replace If Exists Other Wise Raise Error"
        )

    parse.add_argument(
        '--order',
        type=str,
        default= defaults['order'],
        help="Order For Making Template. Must Be `Order Pattern`. Use `'#'` For Default Order."
        )

    parse.add_argument(
        "--string",
        type=str,
        default= defaults['string'],
        help="Generate Order From String. Use For Making Order From Text. This Options Override `--order`",
    )

    parse.add_argument(
        '--length',
        type=int,
        default = defaults['length'],
        help="Options Call When Use `--string` Options Set Length For Generating Order. `None` Means Order Length same as String Length."
    )

    parse.add_argument(
        '--repeat',
        type=int,
        default = defaults['repeat'],
        help= "Repeat Template Order For Generating Blocks."
    )

    parse.add_argument(
        '--size',
        type=int,
        default = defaults['size'],
        help= "Size For Making How Many Blocks If Use Default Order or Order is `None`"
    )

    parse.add_argument(
        '--saveorder',
        action = 'store_true' if not defaults['saveorder'] is True else 'store_false',
        default = defaults['saveorder'],
        help= "Saving Order to Order Store `Name`"
    )

    arguments = {**vars(parse.parse_args())}

    _space = spacer('-', None, 0)

    cprint(_space)
    cprint(center('<<< MOSAICI APP :: Making Template >>>'), 'title')


    if '.' not in arguments['file']:
        cprint("/> File Format Adding ", 'work')
        arguments['file'] = f"{arguments['file']}.tt"

    if is_name(arguments['file']):
        cprint("/> Validate Path To Default Directory ", 'work')
        arguments['file'] = arguments['file'].removeprefix("'").removesuffix("'")
        arguments["file"] = path_join(templates_dir, arguments["file"])

    if x:= arguments['string']:
        cprint('/> Generating Order From String ', 'work')
        arguments['order'] = m_act.from_string(x, arguments['length'])


    cprint("/> Making Template Start Generating ", 'work')
    try:
        t0 = monotonic()
        execute = m_act.make_template(
            arguments['repeat'],
            arguments['size'],
            arguments['order'],
            arguments['file'],
            arguments['replace'],
            )

        cprint(f"~> {execute} ", 'result')

        if arguments['saveorder']:
            cprint('/> Saving Order To Order Store ', 'work')
            name = basename(arguments['file'])
            temp = {
                name: {
                    'order': arguments['order'],
                    'repeat': arguments['repeat']
                    }
                }

            Json.update(temp, order_store)
            cprint('~> Order is Saved in Order Store ', 'result')

        t1 = monotonic()

        cprint(f"!> TIME: {t1 - t0:.3f}", 'time')
        cprint(f"</ Template is Created />", 'done')
    except Exception as err:
        err = error(err, 'Use `--replace` Options For Forced Write File')
        cprint(err)
    finally:
        cprint(_space)

    return 0

def mosaici_app(parse: argparse.ArgumentParser) -> int:
    defaults = CONFIG['mosaici_app_default']
    templates_dir = CONFIG['default_paths']["templates_dir"]

    parse.add_argument(
        '--template',
        type=str,
        default = defaults["template"],
        help="Templates Path or Name if Exists in Template Dir"
    )

    parse.add_argument(
        '--mode',
        type=str,
        choices= ['data', 'mosaic', 'enc', 'dec', 'encrypt', 'decrypt'],
        default = defaults["mode"],
        help="Mode Action `mosaic` for Data To Mosaic, `data` for Mosaic To Data"
    )

    parse.add_argument(
        '--text',
        type=str,
        default= None,
        help="Text For Mosaici or Back To Data From Mosaici"
    )

    parse.add_argument(
        '--file',
        type=str,
        default= None,
        help="File Path"
    )

    parse.add_argument(
        '--res',
        type=str,
        default= None,
        help="Result File Path if Use --text This Option is Optional Other Wise Must Define Path"
    )

    parse.add_argument(
        '--startblock',
        type = int,
        default = 0,
        help="Select Start BLock for Action"
    )

    arguments = {**vars(parse.parse_args())}
    _space = spacer('-', None, 0)

    cprint(_space)
    cprint(center('<<< MOSAICI APP :: Mosaici >>>'), 'title')
    error_happen = False

    t0 = monotonic()
    if is_name(arguments['template']):
        cprint('/> Get Template From Templates and Check', 'work')

        temp = arguments['template']

        if '.' not in temp:
            temp = f'{temp}.tt'

        valid = os.path.realpath(path_join(templates_dir, temp))
        arguments['template'] = (valid, 256)

        if not os.path.isfile(valid):
            error_happen = True
            err = error(NameError, 'Template Name Not Exists in Templates')
            cprint(err, 'err')
    else:
        cprint('/> Template Validation Path and Check', 'work')

        valid = os.path.realpath(arguments['template'])
        if not os.path.isfile(valid):
            error_happen = True
            err = error(FileNotFoundError, 'Not Find Template File in Path')
            cprint(err, 'err')

        arguments['template'] = (valid, 256) 

    cprint('/> Mode Convert To Type', 'work')
    match arguments['mode']:
        case 'mosaic' | 'enc' | 'encrypt':
            arguments['mode'] = 'data'
        case 'data' | 'dec' | 'decrypt':
            arguments['mode'] = 'indexes'

    cprint('/> Result File Validation', 'work')
    arguments['res'] = None if arguments['res'] is None else os.path.realpath(arguments['res'])

    if arguments['text'] and not error_happen:
        cprint('/> Text To Action', 'work')
        if arguments['mode'] == 'indexes':
            cprint('/> Text To Indexes Object', 'work')
            arguments['text'] = m_act.Indexes(arguments['text'])
        else:
            cprint('/> Text To Unicode Binarray Object', 'work')
            arguments['text'] = arguments['text'].encode('utf-8')
        try:
            cprint('/> Mosaic Action is Active', 'work')

            action = m_act.mosaic_file(
                arguments['template'],
                arguments['text'],
                arguments['res'],
                arguments['startblock'],
                arguments['mode'],
            )

            cprint('/> Result Validate', 'work')
            if isinstance(action, bytes):
                action = action.decode('utf-8')
                action = f'Text: {"".join(action)}'

            elif isinstance(action, (str, m_act.Indexes)):
                action = f'Mosaic : {"".join(action)}'

            elif isinstance(action, int):
                action = "Write To Result File Path"

            cprint(f'~> {action}', 'result')
        except Exception as err:
            error_happen = True
            err = error(err)
            cprint(err, 'err')

    if arguments['file'] and not error_happen:
        cprint('/> File To Action', 'work')
        arguments['file'] = os.path.realpath(arguments['file'])

        try:
            cprint('/> Mosaic Action is Active', 'work')
            action = m_act.mosaic_file(
                arguments['template'],
                arguments['file'],
                arguments['res'],
                arguments['startblock'],
                arguments['mode']
            )

            cprint(f'~> File : {action}', 'result')
        except Exception as err:
            error_happen = True
            err = error(err)
            cprint(err, 'err')

    t1 = monotonic()

    cprint(f"!> TIME: {t1 - t0:.3f}", 'time')

    if error_happen:
        cprint(f"</ !! Mosaici Working is Problem Check Arguments And `TryAgain` !! />", 'warning')
    else:
        cprint(f"</ Mosaici Working is Done />", 'done')

    cprint(_space)
    return 0

def main(argv: Sequence[str] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    parse = argparse.ArgumentParser(
        'Mosaici',
        description= "Mosaici Protocol For Coverting Data To Indexes Of Pattern."
        )

    parse.add_argument(
        '--version',
        '-V',
        action = 'version',
        version=f'%(prog)s {VERSION}'
    )

    defaults = CONFIG['app']
    template_call = defaults['template_call']
    manage_call = defaults['manage_call']

    if len(argv) >= 1:
        if argv[0] in template_call:
            return templates_app(parse)
        elif argv[0] in manage_call:
            return manage(parse)
        else:
            return mosaici_app(parse)

    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
