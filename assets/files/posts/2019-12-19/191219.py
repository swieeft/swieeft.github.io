# A) 3.1


def right_justify(s):
    string = ' '*(70-len(s)) + s
    print(string)


right_justify('monty')

# A) 3.2
# (1)


def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')


do_twice(print_spam)

## (2), (3), (4)


def do_twice(f, s):
    f(s)
    f(s)


def print_twice(bruce):
    print(bruce)
    print(bruce)


do_twice(print_twice, 'spam')

# (5)


def do_four(value):
    print_twice(value)
    print_twice(value)


do_four('four')

"""
def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_four(print_twice, 'four')
"""

# A) 3.3


def gridraw(col, row):
    while col > 0:
        col -= 1
        print('+ - - - - '*row, end='')
        print('+')
        rowCount = 0
        while rowCount < 4:
            rowCount += 1
            print('|         '*row, end='')
            print('|')
        if col == 0:
            print('+ - - - - '*row, end='')
            print('+')
