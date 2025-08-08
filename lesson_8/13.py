"""
Link: https://www.codewars.com/kata/52efefcbcdf57161d4000091
"""


def count(s):
    result = {}
    for i in s:
        if i not in result:
            result[i] = s.count(i)
    return result


print(count('aba'))
