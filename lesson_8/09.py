"""
Link: https://www.codewars.com/kata/588453ea56daa4af920000ca
"""


def array_packing(arr):
    return sum(val << (8 * index) for index, val in enumerate(arr))


print(array_packing([24, 85, 0]))
