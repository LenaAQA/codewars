"""
Кевин замечает, что у него заканчивается место!
Напишите функцию, которая удаляет пробелы из значений и возвращает массив,
показывающий уменьшение пространства.
Например, выполнение этой функции для массива
['i', 'have','no','space']даст['i','ihave','ihaveno','ihavenospace']
Link: https://www.codewars.com/kata/56576f82ab83ee8268000059
"""


def spacey(array):
    last = ""
    result = []
    for i in array:
        last += i
        result.append(last)
    return result


print(spacey(['kevin', 'has', 'no', 'space']))
