# qargs (quick arguments)

**NOTE:** `qargs` is still being actively developed and it's API is subject to
change

`qargs` is an argument parser.

`qargs` is fast and easy to use. It is great for rapid prototyping and CLI
utilities that need to minimize startup time.

`qargs` uses POSIX style argument syntax (mostly). It was implemented according
to the syntax described by the The Open Group Base Specifications (Chapter 12:
Utility conventions). [The standard can be read
here](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html).
It intentionally deviates from the standard by not implementing
**12.1, 2a and 2b** and **12.2, guideline 9**.


### Why write another argument parser?

Simply put, I don't like how other parsers work. I believe that they are
needlessly difficult to use and most require too much boilerplate code.
Because of this, I frequently found myself writing one-off parsers to meet my
needs. I decided that instead of constantly reinventing the wheel, I needed
more permanent solution; hence `qargs`.


## Installation

`qargs` can be installed with pip: `pip install quick-arguments`


## Example Usage

`qargs` provides a single function, `parse_args`.

Called without any arguments, `parse_args` will do a few handy things for you:
- gather all non-flag arguments in the .operands attribute
- gather all files in the .files attribute
- gather all directories in the .directories attribute
- determine whether to read stdin with the .stdin attribute

```
import qargs

args = qargs.parse_args()

for f in args.files:
    # do a thing to each file
```

`parse_args` can be called with a specification to tell it what flags to look for.
You can provide a short and a long flag as strings that match the following pattern:
`^[a-zA-Z][a-zA-Z0-9-]*$`

```
import qargs

spec = [
    ['c', 'color'],
    ['v', 'verbose'],
]

args = qargs.parse_args(spec)

if args.color:
    # be colorful

if args.verbose:
    # be verbose
```

You can provide a non-string value to capture arguments. If the value evaluates
to True, the argument is blindly captured. If the value is a callable, that
callable is used to validate the argument.

```
import os
import qargs


def validate_config_file(f):
    return os.path.isfile(f) and f.endswith('.conf')


spec = [
    ['c', 'config-file', validate_config_file],
]

args = qargs.parse_args(spec)

with open(args.config_file, 'r') as cf
    # read config file
```

Help text for a flag can be specified by providing a string that does NOT
match the pattern used for flags: `^[a-zA-Z][a-zA-Z0-9-]*$`

```
import qargs

spec = [
    ['c', 'color', 'enable colored output'],
    ['v', 'verbose', 'enable verbose output'],
]

args = qargs.parse_args(spec)

if args.color:
    # be colorful

if args.verbose:
    # be verbose
```
