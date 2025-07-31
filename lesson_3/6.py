# Реализуйте функцию, которая принимает 2 аргумента: stringи separator.
#
# Ожидаемый алгоритм: разбить stringна слова пробелами,
# разбить каждое слово на отдельные символы и соединить их обратно с указанным separator,
# соединить все полученные «слова» обратно в предложение пробелами.
# #
from operator import index


def split_and_merge(string_, separator):
    res = []
    for word in string_.split(" "):
        joined = separator.join(word)
        res.append(joined)
    return " ".join(res)


print(split_and_merge("My name is John", "-"))
print('M-y n-a-m-e i-s J-o-h-n')
