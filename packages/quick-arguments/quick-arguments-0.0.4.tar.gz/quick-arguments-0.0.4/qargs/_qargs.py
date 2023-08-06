# Copyright (C) 2022 Thomas Ellison
# Licensed under the GPL: https://www.gnu.org/licenses/gpl-3.0.txt
# For details: https://gitlab.com/thomasjlsn/qargs/-/blob/main/LICENSE

import sys
from re import match
import os.path as path
from collections import namedtuple

RE_SHORT = r'^-[a-zA-Z0-9]+$'
RE_LONG = r'^--[a-zA-Z0-9-]+$'
RE_ARG = r'^(--?[a-zA-Z-]+|--?)$'
RE_IDENTIFIER = r'^[a-zA-Z][a-zA-Z0-9_]*$'
RE_FLAG = r'^[a-zA-Z][a-zA-Z0-9-]*$'

RE_INT = r'^[-+]?[0-9]+$'
RE_FLOAT = r'^[-+]?[0-9]+\.[0-9]+$'
RE_DIFFERENT_BASE = r'^[-+]?0(b[01]+|o[0-7]+|x[0-9a-f]+)$'
RE_SCIENTIFIC = r'^[-+]?[0-9]+(\.[0-9]+)?[eE][+-]?[0-9]+$'
RE_COMPLEX = r'^[-+]?[0-9]+[-+][0-9]+[jJ]$'


def abort(message):
    '''Write a message to stderr and exit.'''
    sys.stderr.write(f'{message}\n')
    sys.exit(1)


def abort_missing_arg(flag):
    abort(f'no argument was provided to flag "{flag}"')


def abort_unknown_flag(flag):
    abort(f'unknown flag "{flag}"')


def abort_validation_failed(flag, arg, func):
    # TODO better error message?
    abort(
        f'invalid argument "{arg}" for flag "{flag}" '
        f'(validation function "{func.__name__}" failed)'
    )


def normalize_specs(specifications, help_text=True):
    '''Normalizes entries in the specifications table.'''
    specs = []

    if help_text:
        specs.append((None, 'help', False, 'help', 'display this help message'))

    for spec in specifications:
        short, long, capture, help_string = None, None, False, None

        if len(spec) not in range(1, 5):
            raise ValueError(
                'each argument defined in specs must be '
                'a list of 1 to 4 elements'
            )

        for index, item in enumerate(spec):
            if isinstance(item, str):
                # remove leading dashes if args were specified with them
                item = spec[index] = item.lstrip('-')
                if match(RE_FLAG, item):
                    if len(item) == 1:
                        short = item
                    else:
                        long = item
                else:
                    help_string = item
            else:
                capture = item

        # Replace dashes with underscores to make the name a valid python
        # identifier.
        name = str(long if long else short).replace('-', '_')

        specs.append((short, long, capture, name, help_string))

    return specs


def generate_help_text(spec):
    program_name = path.basename(sys.argv[0])
    help_text = f'{program_name} - usage:\n\n'
    padding = max(15 + len(s[3]) for s in spec)

    for short, long, capture, _, help_string in spec:
        line = ''
        if short:
            line += f'-{short} '
            if capture:
                line += 'ARG '
        if long:
            line += f'--{long} '
            if capture:
                line += 'ARG '

        line = line.ljust(padding)

        if help_string:
            line += help_string

        help_text += f'{line}\n'

    return f'{help_text}\n'


def convert_arg_to_number(arg):
    '''Try to convert arguments to their numeric counterpart.'''
    if match(RE_INT, arg) or match(RE_DIFFERENT_BASE, arg):
        return int(arg, 0)
    if match(RE_FLOAT, arg) or match(RE_SCIENTIFIC, arg):
        return float(arg)
    if match(RE_COMPLEX, arg):
        return complex(arg)
    return arg


def validate_arg(validation_function, flag, arg):
    '''Use the function that the user provided in the spec to validate the
    argument.'''
    try:
        if not validation_function(arg):
            abort_validation_failed(flag, arg, validation_function)
    except Exception:
        abort_validation_failed(flag, arg, validation_function)


def parse_args(specifications=[], arguments=[], numbers=True, help_text=True):
    '''
    EXAMPLE USAGE:

        >>> argv = ['-v']
        >>> spec = [
            ['c', 'color'],
            ['f', 'file', True],
            ['v', 'verbose'],
        ]
        >>> args = parse_args(spec, argv)
        >>> args.verbose
        True
        >>> args.color
        False


    ARGUMENTS:

        parse_args takes an optional specification in the following format
        (see "EXAMPLE USAGE" for an example of a simple specification):

            a list of lists where each nested list contains 1-3 values:
                - short flag
                    - a single char
                    - eg. 'v'

                - long flag
                    - a string
                    - eg. 'verbose'

                - capture
                    - any non False value, if callable it is used to
                      validate_arg the given argument
                    - eg. False
                    - optional, if not provided, defaults to False

        If no specification is provided, parse_args defaults to gathering
        files/dirs, and checking whether or not to read stdin.


    RETURN VALUE:

        parse_args returns a namedtuple with the values parsed from a given
        argument list.

        The namedtuple that is returned also contains various values
        independent of the specification:

        - args        list, the argument list provided to parse_args
        - nargs       int, number of arguments provided
        - operands    list, all non-flag arguments that are not captured by a
                      specific flag
        - dirs        list, non-flag arguments that are directories
        - files       list, non-flag arguments that are files
        - stdin       bool, whether or not to read/write stdin

    '''

    if not arguments:
        arguments = sys.argv[1:]

    parsed = {}
    parsed['args'] = arguments
    parsed['nargs'] = len(arguments)
    parsed['operands'] = []
    parsed['files'] = []
    parsed['dirs'] = []
    parsed['stdin'] = False

    # The default keys are to be reserved for use by qargs only.
    reserved_names = list(parsed.keys())

    # Keep track of which option_arguments have been captured by a flag,
    # these — by definition — are not operands.
    option_arg_indexes = []

    # The flags we are looking for.
    short_flags, long_flags = [], []

    if specifications:
        specifications = normalize_specs(specifications, help_text)

        if help_text:
            if '--help' in arguments:
                sys.stderr.write(generate_help_text(specifications))
                sys.exit(1)

        for short, long, _, name, _ in specifications:
            parsed[name] = False

            if short:
                short_flags.append(short)
            if long:
                long_flags.append(long)

            # Make sure reserved names do not get clobbered.
            if name in reserved_names:
                raise ValueError(
                    f'Naming collision caused by argument name "{name}", '
                    f'"{name}" is reserved for use by qargs'
                )

    for index, arg in enumerate(arguments):
        next_index = index + 1

        if arg == '-':
            # A single "-" indicates we should read from stdin.
            parsed['stdin'] = True

        elif arg == '--':
            # All arguments following "--" are to be considered operands.
            parsed['operands'].extend(arguments[next_index:])
            break

        elif match(RE_SHORT, arg):
            flags = arg[1:]

            # Only the last flag in a series of short flags can capture output
            # (eg. in "-asdf", only "f" is able to capture output)
            last_flag = flags[-1]

            for flag in flags:
                if flag not in short_flags:
                    abort_unknown_flag(flag)

            for short, _, capture, name, _ in specifications:
                if last_flag == short and capture:
                    if last_flag not in short_flags:
                        abort_unknown_flag(last_flag)

                    try:
                        option_arg = arguments[next_index]
                    except IndexError:
                        abort_missing_arg(last_flag)

                    if numbers:
                        option_arg = convert_arg_to_number(option_arg)

                    if callable(capture):
                        validate_arg(capture, last_flag, option_arg)

                    if match(RE_ARG, str(option_arg)):
                        if path.exists(option_arg):
                            parsed[name] = option_arg
                            option_arg_indexes.append(next_index)
                        else:
                            abort_missing_arg(last_flag)
                    else:
                        parsed[name] = option_arg
                        option_arg_indexes.append(next_index)
                else:
                    for flag in flags:
                        if flag == short and capture:
                            abort_missing_arg(flag)

                        if flag not in short_flags:
                            abort_unknown_flag(flag)

                        if flag == short:
                            parsed[name] = True

        elif match(RE_LONG, arg):
            flag = arg[2:]

            if flag not in long_flags:
                abort_unknown_flag(flag)

            for _, long, capture, name, _ in specifications:
                if flag == long:
                    if capture:
                        try:
                            option_arg = arguments[next_index]
                        except IndexError:
                            abort_missing_arg(flag)

                        if numbers:
                            option_arg = convert_arg_to_number(option_arg)

                        if callable(capture):
                            validate_arg(capture, flag, option_arg)

                        if match(RE_ARG, str(option_arg)):
                            if path.exists(option_arg):
                                parsed[name] = option_arg
                                option_arg_indexes.append(next_index)
                            else:
                                abort_missing_arg(arg)
                        else:
                            parsed[name] = option_arg
                            option_arg_indexes.append(next_index)
                    else:
                        parsed[name] = True

        else:
            if index not in option_arg_indexes:
                if arg not in parsed['operands']:
                    parsed['operands'].append(arg)

    # Gather files and dirs from given operands
    for operand in parsed['operands']:
        if path.isfile(operand):
            parsed['files'].append(operand)
        elif path.isdir(operand):
            parsed['dirs'].append(operand)

    return namedtuple('arguments', parsed)(**parsed)
