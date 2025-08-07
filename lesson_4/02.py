"""
Создайте функцию, которая принимает целое число в качестве аргумента
и возвращает значение "Even"для четных или "Odd"нечетных чисел.
Link: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
"""


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(2))
