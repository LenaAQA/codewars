"""
Link: https://www.codewars.com/kata/56a24b309f3671608b00003a
"""


def dad_filter(string):
    result = []
    string = string.split()
    for i in string:
        if i.count(",") > 1:
            if string.index(i) != len(string) - 1:
                result.append(i.strip(",") + ",")
            else:
                result.append(i.strip(","))
        else:
            result.append(i)
    return " ".join(result).strip(",")


print(dad_filter('my,,,, my me,,,, money,   '))
