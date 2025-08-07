"""
Link: https://www.codewars.com/kata/580755730b5a77650500010c
"""


def sort_my_string(s):
    return s[::2] + " " + s[1::2]


print(sort_my_string("CodeWars"))
