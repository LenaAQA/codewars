"""
Link: https://www.codewars.com/kata/590c4c342ad5cd6a8700005c
"""


def prefix_sums_to_suffix_sums(prefix_sums):
    total = prefix_sums[-1]
    result = []
    for i, v in enumerate(prefix_sums):
        if i == 0:
            result.append(total)
        else:
            result.append(total - prefix_sums[i - 1])
    return result


print(prefix_sums_to_suffix_sums([1, 3, 6, 10, 15]))
