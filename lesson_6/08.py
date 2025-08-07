"""
Link: https://www.codewars.com/kata/58f8b35fda19c0c79400020f
"""


def all_non_consecutive(arr):
    result = []
    for i in range(len(arr) - 1):
        n = arr[i + 1]
        if n - arr[i] > 1:
            result.append({"i": arr.index(n), "n": n})
    return result


print(all_non_consecutive([1, 2, 3, 4, 6, 7, 8, 10]))
