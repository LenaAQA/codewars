# Обратите внимание, что фразу можно также записать как "3.50"или "three fifty".
# Ваша функция должна возвращать true, если вы общаетесь с Лох-Несским чудовищем,
# и false в противном случае


def is_loch_ness_monster(string):
    k = ["3.50", "tree fiddy", "three fifty"]
    return bool([i for i in k if i in string])


print(is_loch_ness_monster("Your girlscout cookies are ready to ship. Your total comes to tree fiddy"))
