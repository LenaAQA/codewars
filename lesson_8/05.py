"""
Link: https://www.codewars.com/kata/534d0a229345375d520006a0
"""


def power_of_two(x):
    if x < 1:
        return False
    while x % 2 == 0:
        x = x // 2
    return x == 1


print(power_of_two(2361183241434822606846))
