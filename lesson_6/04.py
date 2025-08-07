"""
Link: https://www.codewars.com/kata/53d32bea2f2a21f666000256
"""


def largest(n, xs):
    return sorted(xs)[-n:] if n != 0 else []


print(largest(2, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
