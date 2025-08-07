"""
Link: https://www.codewars.com/kata/5966f6343c0702d1dc00004c
"""


def give_change(amount):
    bills = [100, 50, 20, 10, 5, 1]
    result = []
    for bill in bills:
        count = amount // bill
        result.append(count)
        amount -= count * bill
    return tuple(result[::-1])


print(give_change(365))
