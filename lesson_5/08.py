"""
Это продолжение моего старого ката «Переключатель».
Напишите функцию, которая принимает строку и заменяет все буквы на
их соответствующие позиции в английском алфавите, например, 'a'is 1, 'z'is 26.
Функция не должна учитывать регистр.
Link: https://www.codewars.com/kata/55d6a0e4ededb894be000005
"""


def encode(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in st:
        if i.lower() in alphabet:
            st = st.replace(i, str(alphabet.index(i.lower()) + 1))
    return st


print(encode('abc'))
