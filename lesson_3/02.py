"""
Напишите мне функцию stringy, которая принимает a size и возвращает a string чередующихся 1s и 0s.
Строка должна начинаться с 1.
строка с size6 должна вернуть: '101010'.
Строка с size4 должно вернуть: '1010'.
Строка с size12 должно вернуть: '101010101010'.
Размер всегда будет положительным и будет использовать только целые числа.
Link: https://www.codewars.com/kata/563b74ddd19a3ad462000054
"""


def stringy(size):
    result = ""
    for i in range(size):
        if i % 2 == 0:
            result += str(1)
        else:
            result += str(0)
    return result


print(stringy(5))
