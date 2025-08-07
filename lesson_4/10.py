"""
Завершите функцию nato, которая принимает слово в качестве параметра и возвращает строку,
описывающую это слово с использованием фонетического алфавита НАТО.
Между каждым словом в возвращаемой строке должен быть пробел, а первая буква каждого слова должна быть заглавной.
Для тех из вас, кто не хочет, чтобы ваши пальцы кровоточили, уже есть напечатанный словарь.
Link: https://www.codewars.com/kata/54530f75699b53e558002076
"""


nato_words = [
        "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima",
        "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey",
        "X-ray", "Yankee", "Zulu"
    ]


def nato(word):
    list_word = []
    for i in word:
        for j in nato_words:
            if j[0].lower() == i.lower():
                list_word.append(j)
    return " ".join(list_word)


print(nato("hi"))
