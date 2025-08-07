"""
Link: https://www.codewars.com/kata/5c79c07b4ba1e100097f4e1a
"""


def yoga(classroom, poses):
    result = 0
    for i in classroom:
        s = sum(i)
        for ii in i:
            ss = s + ii
            for j in poses:
                if ss >= j:
                    result += 1
    return result


print(yoga([
    [3, 2, 1, 3],
    [1, 3, 2, 1],
    [1, 1, 1, 2],
], [1, 7, 5, 9, 10, 21, 4, 3]))
