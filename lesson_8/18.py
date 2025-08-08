"""
Link: https://www.codewars.com/kata/55b051fac50a3292a9000025
"""


def filter_string(st):
    return int("".join([i for i in st if i.isdigit()]))


print(filter_string("aa1bb2cc3dd"))
