# Найдите сумму всех кратных nниже чисел.m
#
# Иметь в виду
# nи mявляются натуральными числами (положительными целыми числами)
# mисключен из кратных


def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    res = 0
    for i in range(n, m):
        if i % n == 0:
            res += i
    return res


print(sum_mul(2, 2))

