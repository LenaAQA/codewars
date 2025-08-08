"""
Link: https://www.codewars.com/kata/57fafb6d2b5314c839000195
"""


def remove(s):
    return " ".join([i for i in s.split() if i.count("!") != 1])


print(remove('!!!Hi !!hi!!! !hi'))
