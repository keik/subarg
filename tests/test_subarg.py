# -*- coding: utf-8 -*-

from subarg import parse


def test_parse_no_subarg():
    args = parse('-a b --c d -e'.split())
    assert args == ['-a', 'b',
                    '--c', 'd',
                    '-e']


def test_parse_1l_subarg():
    args = parse('-a b --c [ d -e f ] -g'.split())
    assert args == ['-a', 'b',
                    '--c', ['d', '-e', 'f'],
                    '-g']


def test_parse_multiple_1l_subarg():
    args = parse('-a b --c [ d -e f ] -g [ h -i j ] -k'.split())
    assert args == ['-a', 'b',
                    '--c', ['d', '-e', 'f'],
                    '-g', ['h', '-i', 'j'],
                    '-k']


def test_parse_2l_subarg():
    args = parse('-a b --c [ d -e [ f -g h ] i ] -j'.split())
    print(args)
    assert args == ['-a', 'b',
                    '--c', ['d',
                            '-e', ['f', '-g', 'h'],
                            'i'],
                    '-j']


def test_parse_multiple_2l_subarg():
    args = parse('-a b --c [ d -e [ f -g h ] i ] -j [ k -l [ m -n o ] p ] q'.split())
    print(args)
    assert args == ['-a', 'b',
                    '--c', ['d',
                            '-e', ['f', '-g', 'h'],
                            'i'],
                    '-j', ['k',
                           '-l', ['m', '-n', 'o'],
                           'p'],
                    'q']
