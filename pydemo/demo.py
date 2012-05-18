import argparse

def fibs(n):
    '''Return *n* th fibonacci number.

    Example usage::

        >>> fibs(7)
        13

        >>> [ fibs(n) for n in xrange(18) ]
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibs(n - 1) + fibs(n - 2)


def hello_world():
    '''Prints **Hello, world!**.

    Example usage::

        >>> hello_world()
        Hello, world!

    '''
    print 'Hello, world!'


def main():
    parser = argparse.ArgumentParser(prog='pydemo',
    description='''A small package to show off docstrings and stuff''')
    parser.add_argument('integer', metavar='N',
            help="an integer for fibs", type=int)

    args = parser.parse_args()

    print fibs(args.integer)

    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
