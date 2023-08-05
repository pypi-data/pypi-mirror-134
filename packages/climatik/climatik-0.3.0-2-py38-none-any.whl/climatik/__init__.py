"""
climatik

Create command line interface from function definitions.
Each function will be a subcommand of your application.
"""

import inspect
import argparse
from typing import Callable, Optional, TypedDict, Dict, Any,  Union, get_origin, get_args

__version__ = "0.3.0"

class CommandType(TypedDict):
    help:Optional[str]
    description:Optional[str]
    func:Callable
    args:Dict[str, Any]

commands:Dict[str,CommandType] = {}

def is_optional(field):
    return get_origin(field) is Union and \
           type(None) in get_args(field)

def get_parser(*args, **kwargs) -> argparse.ArgumentParser:
    """Build command line parser
    
    Arguments are passed to `argparse.ArgumentParser` constructor
    """
    parser = argparse.ArgumentParser(*args, **kwargs)
    parser.set_defaults(func=lambda *a,**k: parser.print_help())
    subparsers = parser.add_subparsers()
    for name, command in commands.items():
        s_parser = subparsers.add_parser(name, help=command['help'], description=command['description'])
        for s_name, arg in command['args'].items():
            s_parser.add_argument(s_name, **arg)
        s_parser.set_defaults(func=command['func'])
    return parser


def execute(parser:argparse.ArgumentParser):
    """Execute command line from given parser"""
    nsargs = parser.parse_args()
    args = vars(nsargs)
    func = args['func']
    del args['func']
    kwargs = { k.replace("-","_"): args[k] for k in args }
    func(**kwargs)


def run(prog:str=None, usage:str=None, description:str=None, **kwargs):
    """Run your application"""
    parser = get_parser(prog=prog, usage=usage, description=description, **kwargs)
    execute(parser)


def command(fnc:Callable):
    """Build subcommand from function

    Subcommand name will be the function name and arguments are parsed to build the command line.

    Each positional argument will be a positional paramenter.
    Each optional argument will be an optional flag.
    Type hints are used to covert types from command line string.
    An argument with `bool` type is converted to an optional flag parameter (with default sematic as "False")
    To create an optional positional paramenter, use the `typing.Optional` type as hint with the parameter type,
    e.g. `Optional[str]`

    Function docstring is used to set command's help and description.

    
        @command
        def one(name, debug:bool, value="default", switchoff=True):
            "First subcommand"
            ...

        @command
        def two(name:Optional[str] = None, long_param = None):
            "Second subcommand"
            ...

    gives:

        $ script -h
        usage: script [-h] {one,two} ...

        positional arguments:
        {one,two}
            one       First subcommand
            two       Second subcommand

        optional arguments:
        -h, --help  show this help message and exit

        $ script one -h
        usage: script one [-h] [--debug] [--value VALUE] [--switchoff] name

        First subcommand

        positional arguments:
        name

        optional arguments:
        -h, --help     show this help message and exit
        --debug
        --value VALUE
        --switchoff

        $ script two -h
        usage: script two [-h] [--long-param LONG_PARAM] [name]

        Second subcommand

        positional arguments:
        name

        optional arguments:
        -h, --help            show this help message and exit
        --long-param LONG_PARAM

    """

    #parser = argparse.ArgumentParser(description=fnc.__doc__)
    help:Optional[str] = None
    try:
        help = fnc.__doc__ or ""
        help = help.split('\n')[0].strip()
    except (AttributeError, IndexError):
        help = None

    command:CommandType = {
        'help' : help,
        'description' : fnc.__doc__,
        'func' : fnc,
        'args' : {},
    }

    sig = inspect.signature(fnc)
    for k in sig.parameters:
        param = sig.parameters[k]
        name = param.name
        arg = {}

        # let's use annotation type for argument type
        if not param.annotation is param.empty:
            # TODO: this is ugly.. may be it's better in python 3.10 with `match`?
            if is_optional(param.annotation):
                arg['type'] = get_args(param.annotation)[0]
            else:
                arg['type'] = param.annotation

        # if param has default value, argument is optional
        if not param.default is param.empty:
            # make it a flag but not if type is Optional
            if is_optional(param.annotation):
                arg['nargs'] = "?"
            else:
                name = "--"+name
            arg['default'] = param.default
            
            if 'type' not in arg:
                arg['type'] = type(param.default)

        # we don't want arguments with type "None". default to "str"
        if 'type' in arg and arg['type'] == type(None):
            arg['type'] = str

        # if argument type is bool, the argument become a switch
        if 'type' in arg and arg['type'] is bool:
            if not name.startswith('--'):
                name = "--"+name
            if not 'default' in arg:
                arg['action']="store_true"
            else:
                arg['action']="store_" + str(not arg['default']).lower()
                del arg['default']
            del arg['type']

        # "arg_name" to "arg-name"
        name = name.replace("_", "-")
        command['args'][name] = arg

    commands[fnc.__name__] = command
    return fnc


if __name__=="__main__":
    @command
    def one(name, debug:bool, value="default", switchoff=True):
        "First subcommand"
        print(f"name: {name!r}, debug: {debug!r}, value: {value!r}, switchoff: {switchoff!r}")

    @command
    def two(name:Optional[str] = None, long_param = None):
        "Second subcommand"
        print(f"name: {name!r}, long_param: {long_param!r}")

    run()