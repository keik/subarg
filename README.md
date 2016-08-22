# subarg

[![License](https://img.shields.io/pypi/l/subarg.svg?style=flat-square)](https://github.com/keik/subarg/blob/master/LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/subarg.svg?style=flat-square)](https://pypi.python.org/pypi/subarg)
[![PyPI](https://img.shields.io/pypi/v/subarg.svg?style=flat-square)](https://pypi.python.org/pypi/subarg)
[![Travis CI](https://img.shields.io/travis/keik/subarg.svg?style=flat-square)](https://travis-ci.org/keik/subarg)
[![Coverage Status](https://img.shields.io/coveralls/keik/subarg.svg?style=flat-square)](https://coveralls.io/github/keik/subarg)

Parse sub-arguments in `[` and `]` recursively.


## Usage

Basically

```
>>> import subarg
>>> argv = ['--foo', 'bar', '--buz', '[', 'qux', '--quux', 'corge', ']']
>>> subarg.parse(argv)
['--foo', 'bar', '--buz', ['qux', '--quux', 'corge']]
```

It's useful to pass `sys.argv` directly.
For example, with *example.py* like

```python
import sys
import subarg

args = subarg.parse(sys.argv)

print(args)
```

and execute belows, then arguments would be parsed like

```
% python example.py --foo bar --buz [ qux --quux corge ]
['example.py', '--foo', 'bar', '--buz', ['qux', '--quux', 'corge']]
```


### Collaborate with `argparse`

We can collaborate with `argparse`.

```python
import sys
import subarg
from argparse import ArgumentParser

sys.argv = subarg.parse(sys.argv)

parser = ArgumentParser()
parser.add_argument('--foo')
parser.add_argument('--buz')
args = parser.parse_args()

print(args)
```

Then

```
% python example.py --foo bar --buz [ qux --quux corge ]
Namespace(buz=['qux', '--quux', 'corge'], foo='bar')
```


## Test

```
make test
```


## License

MIT (c) keik
