"""
Link: https://www.codewars.com/kata/55968ab32cf633c3f8000008
"""


def initials(name):
    n = name.title().split()
    ln = n[-1]
    fn = []
    for i in n[:-1:]:
        fn.append(i[0])
    return f"{'.'.join(fn)}.{ln}"


print(initials('Barack hussein obama'))
