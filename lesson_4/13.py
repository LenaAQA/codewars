"""
DropCaps означает, что первая буква начального слова абзаца должна быть заглавной, а остальные — строчными,
как в газете.
Но для разнообразия давайте сделаем это для каждого слова в данной строке.
Ваша задача — начать с заглавной буквы каждое слово, длина которого больше 2, оставив слова меньшего размера как есть.
*также должно работать с начальными и конечными пробелами и заглавными буквами.
"apple" => "Apple"
"apple of banana" => "Apple of Banana"
"one space" => "One Space"
"space WALK" => "Space Walk"
Примечание: вам будет предоставлено по крайней мере одно слово,
и вы должны принять строку в качестве входных данных и вернуть строку в качестве выходных данных.
Link: https://www.codewars.com/kata/559e5b717dd758a3eb00005a
"""


def drop_cap(words):
    new_words = words
    for word in words.split():
        if len(word) > 2:
            new_words = new_words.replace(word, word.capitalize())
    return new_words


print(drop_cap("one   space"))
