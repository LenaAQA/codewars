"""
Link: https://www.codewars.com/kata/559cc2d2b802a5c94700000c
"""


def consecutive(arr):
    return max(arr) - min(arr) + 1 - len(arr) if len(arr) > 1 else 0


print(consecutive([4, 8, 6]))
