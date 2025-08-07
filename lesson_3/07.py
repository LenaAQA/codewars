"""
Найдите сумму всех кратных n ниже чисел m.
Иметь в виду n и m являются натуральными числами (положительными целыми числами) m исключен из кратных
Link: https://www.codewars.com/kata/57241e0f440cd279b5000829
"""


def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    result = 0
    for i in range(n, m):
        if i % n == 0:
            result += i
    return result


print(sum_mul(2, 2))
