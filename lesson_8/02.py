"""
Link: https://www.codewars.com/kata/55ccdf1512938ce3ac000056
"""


def is_loch_ness_monster(string):
    monster = ["3.50", "tree fiddy", "three fifty"]
    return bool([i for i in monster if i in string])


print(is_loch_ness_monster("Your girlscout cookies are ready to ship. Your total comes to tree fiddy"))
