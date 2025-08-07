"""
Реализуйте функцию, которая принимает 2 аргумента: string и separator.
Ожидаемый алгоритм: разбить string на слова пробелами,
разбить каждое слово на отдельные символы и соединить их обратно с указанным separator,
соединить все полученные «слова» обратно в предложение пробелами.
Link: https://www.codewars.com/kata/57280481e8118511f7000ffa
"""


def split_and_merge(string_, separator):
    result = []
    for word in string_.split():
        word = separator.join(word)
        result.append(word)
    return " ".join(result)


print(split_and_merge("My name is John", "-"))
