# -*- coding: utf-8 -*-


def parse(argv, level=0):
    nargs = []

    for i in range(len(argv)):

        if argv[i] == '[':
            level += 1

            if level == 1:
                index = i + 1

        elif argv[i] == ']':
            level -= 1
            sub = argv[index:i]

            if level == 0:
                nargs.append(parse(sub, level))

        elif level == 0:
            nargs.append(argv[i])

    return nargs
