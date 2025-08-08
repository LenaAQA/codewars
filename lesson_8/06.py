"""
Link: https://www.codewars.com/kata/6071ef9cbe6ec400228d9531
"""


def calculator(txt):
    lst = txt.split()
    x = len(lst[0])
    y = len(lst[2])
    z = "."
    res = ""
    d = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '//': lambda x, y: x // y,
    }


print(calculator("..... + ..............."))
