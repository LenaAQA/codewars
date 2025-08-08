"""
Link: https://www.codewars.com/kata/55960bbb182094bc4800007b
"""


def insert_dash(num):
    num = [int(i) for i in str(num)]
    result = []
    count = len(num)
    for i in range(len(num)):
        count -= 1
        result.append(str(num[i]))
        if count > 0:
            if num[i] % 2 != 0 and num[i + 1] % 2 != 0:
                result.append("-")
    return "".join(result)


print(insert_dash(454793))
