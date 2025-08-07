"""
Это ката задумано как небольшое испытание для моих учеников.
Создайте функцию, которая принимает строковый аргумент и возвращает ту же строку,
из которой удалены все гласные (гласные — «a», «e», «i», «o», «u»).
Пример (Вход -> Выход):
"drake" --> "drk"
"aeiou" --> ""
remove_vowels("drake") // => "drk"
remove_vowels("aeiou") // =>
Link: https://www.codewars.com/kata/58640340b3a675d9a70000b9
"""


def remove_vowels(strng):
    return "".join([i for i in strng if i not in "aeiou"])


print(remove_vowels("drake"))
