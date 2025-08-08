"""
Link: https://www.codewars.com/kata/586560a639c5ab3a260000f3
"""


def rotate(str_):
    result = []
    for i in str_:
        result.append(str_.replace(str_, str_[1:] + str_[0]))
        str_ = str_[1:] + str_[0]
    return result


print(rotate("Hello"))
