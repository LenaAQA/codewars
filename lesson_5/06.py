"""
Напишите функцию, которая принимает два строковых параметра search_text и full_text
возвращает количество раз, когда символ search_text встречается в строке full_text.
Перекрытие не допускается: "aaa"содержит 1экземпляр "aa", а не 2.
search_text никогда не будет пустым.
Link: https://www.codewars.com/kata/5168b125faced29f66000005
"""


def solution(full_text: str, search_text: str) -> int:
    res = 0
    for i in full_text:
        if search_text in full_text:
            full_text = full_text.replace(search_text, "0" * len(search_text), 1)
            print(full_text)
            res += 1
    return res


print(solution("ntnntnntntnntnnnntntnntnnntnntnnt", "ntn"))
