"""
Link: https://www.codewars.com/kata/5442e4fc7fc447653a0000d5
"""


def greatest_distance(arr):
    positions = {}
    max_distance = 0
    for i, num in enumerate(arr):
        if num not in positions:
            positions[num] = i
        else:
            distance = i - positions[num]
            max_distance = max(max_distance, distance)
    return max_distance


print(greatest_distance([9, 7, 1, 2, 3, 7, 0, -1, -2]))
