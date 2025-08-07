"""
Link: https://www.codewars.com/kata/555de49a04b7d1c13c00000e
"""


def add(*args):
    result = 0
    args = list(args)
    for i in range(1, len(args) + 1):
        ii = args[i - 1] / i
        result += ii
    return round(result)


print(add(4, -3, -2))
