# Создайте функцию, которая принимает целое число в качестве аргумента
# и возвращает значение "Even"для четных или "Odd"нечетных чисел.


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(2))
