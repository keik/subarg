# subarg

Parse sub-arguments in `[` and `]` recursively.


## Usage

With *example.py* like

```python
import sys
import subarg

args = subarg.parse(sys.argv)

print(args)
```

And execute belows, then arguments would be parsed like

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
