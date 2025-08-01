# Сможете ли вы найти иголку в стоге сена?
#
# Напишите функцию findNeedle(), которая принимает arrayполный мусор, но содержит один"needle"
#
# После того как ваша функция обнаружит иглу, она должна вернуть сообщение (в виде строки) следующего содержания:
#
# "found the needle at position "плюс indexон нашел иголку, так что:
#
# Пример (Вход -> Выход)
#
# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"
# Примечание: в COBOL это должно возвращать "found the needle at position 6"


def find_needle(haystack):
    return f"found the needle at position {haystack.index("needle")}"


print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
