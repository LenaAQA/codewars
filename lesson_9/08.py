"""
Link: https://www.codewars.com/kata/59269e371a640c0e98000085
"""


def x_plus_y(s):
    if not set(s).issubset({'0', '1'}):
        return 0
    s = list(s)
    steps = 0
    while '1' in s[:-1]:
        for i in range(len(s) - 1):
            if s[i] == '1':
                s[i] = '0'
                s[i + 1] = '0' if s[i + 1] == '1' else '1'
                steps += 1
                break
    if s and s[-1] == '1':
        steps += 1
    return steps


print(x_plus_y("011101010101"))
print(x_plus_y("101010101010101010"))
