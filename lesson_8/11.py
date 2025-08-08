"""
Link: https://www.codewars.com/kata/55b54be931e9ce28bc0000d6
"""


def position(x, y, n):
    a = (y / x) - (x - 1) / 2
    return int(a + n)


print(position(4, 14, 3))
