#!python

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

"""NanamiLang REPL"""

import argparse
import atexit
import os
import readline
import sys
import time

import nanamilang.datatypes
import nanamilang.formatter
from nanamilang.shortcuts import truncated
from nanamilang import module, loader
from nanamilang.contrib.window import Window
from nanamilang.builtin import BuiltinFunctions, BuiltinMacros
from nanamilang.bdb import BuiltinMacrosDB, BuiltinFunctionsDB
from nanamilang import __version_string__, __author__, __project_license__

readline_history_file_path = os.path.join(
    os.path.expanduser("~"), ".nanamilang_history")
try:
    readline.set_history_length(1000)
    readline.read_history_file(readline_history_file_path)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, readline_history_file_path)

# Initialize Builtin* DB ...
BuiltinMacrosDB.initialize(BuiltinMacros)
BuiltinFunctionsDB.initialize(BuiltinFunctions)

readline.parse_and_bind("tab: complete")
readline.parse_and_bind('set blink-matching-paren on')

repl_exit_fun_names: list = ['exit!', 'bye!', 'exit', 'bye', 'quit', 'quit!']
builtin_names = BuiltinMacrosDB.names() + BuiltinFunctionsDB.names() + repl_exit_fun_names


def complete(t: str, s: int):
    """NanamiLang REPL complete() function for GNU readline"""
    return ([name for name in builtin_names if name.startswith(t)] + [None]).__getitem__(s)


readline.set_completer(complete)


def check_whether_user_want_to_exit(m: module.Module) -> None:
    """
    1. m.tokenized() contains only ONE token:
    2. that token is a type() of Token.Identifier
    3. that token dt().origin() is something from repl_exit_fun_names

    :param m: REPL module instance which used to evaluate user's inputs
    """

    if len(m.tokenized()) == 1:
        first = m.tokenized()[0]
        if first.type() == 'Identifier':
            if first.dt().origin() in repl_exit_fun_names:
                name = first.dt().origin()
                print(f'Type ({name}) or press "Control+D" or "Control+C" to exit REPL')


def main():
    """NanamiLang REPL Main function"""

    parser = argparse.ArgumentParser('NanamiLang REPL')
    parser.add_argument('--no-greeting',
                        help='Greeting can be disabled',
                        action='store_true', default=False)
    parser.add_argument('--include-traceback',
                        help='Include exception traceback',
                        action='store_true', default=False)
    parser.add_argument('--show-measurements',
                        help='In addition to (measure...)',
                        action='store_true', default=False)
    parser.add_argument('--license',
                        help='Show license of NanamiLang',
                        action='store_true', default=False)
    parser.add_argument('--version',
                        help='Show version of NanamiLang',
                        action='store_true', default=False)

    args = parser.parse_args()

    # GNU GPL v2 may require these options

    if args.version:
        print('NanamiLang', __version_string__)
        return 0

    if args.license:
        print('License is', __project_license__)
        return 0

    # Collect Python 3 version into single string
    p_ver = '.'.join([str(sys.version_info.major),
                      str(sys.version_info.minor),
                      str(sys.version_info.micro)])

    # First, good boys always should start with the greeting
    print('NanamiLang', __version_string__, 'by', __author__, 'on Python', p_ver)
    if not args.no_greeting:
        print('History path is:', readline_history_file_path)
        if not os.environ.get('NANAMILANG_PATH'):
            print('\nNANAMILANG_PATH environment variable has not been set!\n')
        print('History of computations is stored in *1, *2, and *3 global bindings')
        print('The most recent exception occurred (which we handle) stored in "*e"')
        print('Type (doc function-or-macro) to see function-or-macro documentation')
        print('     Since version 0.15.0: doc is a part of NanamiLang Standard Lib')
        print('     Fetch a https://nanamilang.jedi2light.moe/pkg/stdlib.nml, then')
        print('     include target directory to NANAMILANG_PATH, then do following')
        print("     (require 'stdlib)    ;; require NanamiLang Standard Lib module")
        print('     (def doc stdlib/doc) ;; make an alias to access doc as earlier')
        print('Type (exit!), (bye!), press "Control+D" or "Control+C" to exit REPL')

    # Since nanamilang.builtin.BuiltinFunctions provides install() method,
    # we can install functions to help the user to exit NanamiLang REPL in easy way!
    for repl_exit_fun_name in repl_exit_fun_names:
        BuiltinFunctions.install(
            {
                'name': repl_exit_fun_name,
                'forms': [f'({repl_exit_fun_name})'],
                'docstring': 'Exit NanamiLang REPL environment with a zero exitcode'
            },
            lambda _: sys.exit(0)
        )

    m = module.Module(name='REPL')  # <- create a nanamilang module instance and ...

    computations = Window(3)  # <- initialize a window to manage computation history

    # Initialize REPL globals with nil value (Clojure REPL-like)

    e = m.environ()
    e.set('*e', nanamilang.datatypes.Nil('nil'))
    e.set('*1', nanamilang.datatypes.Nil('nil'))
    e.set('*2', nanamilang.datatypes.Nil('nil'))
    e.set('*3', nanamilang.datatypes.Nil('nil'))

    # Initialize NanamiLang Loader mechanism ...
    loader.Loader.initialize(
        module.Module,
        loader.LocalIOLoader, include_tb=args.include_traceback)

    # Here, we finally can start the main loop, hooray!
    while True:
        try:
            # First, let the user enter something they want to
            src = input('REPL> ')
            __repl_got_input__ = time.perf_counter()
            # Skip source evaluation in case of the empty input ...
            if not src:
                continue
            # Call m.prepare() to prepare current user's expression
            m.prepare(src)
            # Show tips in case user want to exit NanamiLang REPL script
            check_whether_user_want_to_exit(m)
            # Iterate through results, if some of them - NException, handle it
            for dt in m.evaluate().results():
                if isinstance(dt, nanamilang.datatypes.NException):
                    e.set('*e', dt)
                    # Store most recent NException data type in *e global variable
                    if not args.include_traceback:
                        print(truncated(dt.format(src=src), 67))
                    else:
                        print('\n\b',
                              truncated(
                                  dt.format(src=src,
                                            include_traceback=args.include_traceback), 67))
                else:
                    computations.push(dt)  # <- push computation result to computations hst
                    print(truncated(dt.format(), 67))  # <- and print a computation result!
            # Populate computations history ###############################################
            e.set('*1', computations.get(0, default=e.get('*1')))
            e.set('*2', computations.get(1, default=e.get('*2')))
            e.set('*3', computations.get(2, default=e.get('*3')))
            ###############################################################################
            # If '--show-measurements' has been passed, show all the available measurements
            if args.show_measurements:
                stats = {'[REPL]': time.perf_counter() - __repl_got_input__}
                # Sadly, we do not count dictionary update operation
                stats.update(m.measurements())
                # Also, we don't count: iterating, unpacking, rounding, formatting, printing
                print(*[f'{stat} took {took:.5f} seconds.' for stat, took in stats.items()])
        except (EOFError, KeyboardInterrupt):
            print("Bye for now!")
            break

    return 0

    # Return 0 to system and exit NanamiLang REPL script after playing around with NanamiLang


if __name__ == "__main__":
    main()
