"""
Link: https://www.codewars.com/kata/586538146b56991861000293
"""


from preloaded import NATO # NATO['A'] == 'Alfa', etc


def to_nato(words: str) -> str:
    result = []
    for i in "".join(words.split()):
        if i.isalpha():
            result.append(NATO[i.upper()])
        else:
            result.append(i)
    return " ".join(result)
