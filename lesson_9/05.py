"""
Link: https://www.codewars.com/kata/5a86073fb17101e453000258
"""


def sort_emotions(arr, order):
    res_true = []
    emotions = [":D", ":)", ":|", ":(", "T_T"]
    for j in emotions:
        for _ in range(len(arr) + 1):
            if j in arr:
                res_true.append(j)
                arr.remove(j)
    res_false = res_true[::-1]
    return res_true if order else res_false


print(sort_emotions([':(', 'T_T', ':(', ':(', ':|', 'T_T', ':)', ':|'], False))
