"""
Link: https://www.codewars.com/kata/559e5b717dd758a3eb00005a
"""


def drop_cap(words):
    for i in words.split():
        if len(i) > 2:
            words = words.replace(i, i.title())
    return words


print(drop_cap('apple'))
