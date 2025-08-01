# Завершите функцию nato, которая принимает слово в качестве параметра и возвращает строку,
# описывающую это слово с использованием фонетического алфавита НАТО .
#
# Между каждым словом в возвращаемой строке должен быть пробел, а первая буква каждого слова должна быть заглавной.
#
# Для тех из вас, кто не хочет, чтобы ваши пальцы кровоточили, в этой ката уже есть напечатанный словарь.


nato_words = [
        "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima",
        "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey",
        "X-ray", "Yankee", "Zulu"
    ]


def nato(word):
    s = []
    for i in word:
        for j in nato_words:
            if j[0].lower() == i.lower():
                s.append(j)
    return " ".join(s)


print(nato("hi"))
