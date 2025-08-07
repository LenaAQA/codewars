"""
Link: https://www.codewars.com/kata/563f879ecbb8fcab31000041
"""


def factory(x):
    def inner(lst):
        return [i * x for i in lst]
    return inner


print(factory(3)([1, 2, 3]))
