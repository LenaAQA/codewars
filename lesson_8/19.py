"""
Link: https://www.codewars.com/kata/56a946cd7bd95ccab2000055
"""


def lowercase_count(strng):
    return len([i for i in strng if i.islower()])


print(lowercase_count("abcABC123"))
