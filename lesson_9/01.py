"""
Link: https://www.codewars.com/kata/59f70440bee845599c000085
"""


def find_hack(arr):
    result = []
    for i in arr:
        name = i[0]
        score = i[1]
        grades = i[2]
        score_real = grades.count("A") * 30 + grades.count("B") * 20 + grades.count("C") * 10 + grades.count("D") * 5
        if (grades.count("A") + grades.count("B")) == len(grades) and len(grades) >= 5:
            score_real += 20
        if score_real > 200:
            score_real = 200
        if score > 200 or score != score_real:
            result.append(name)
    return result


array = [
    ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
    ["name2", 110, ["B", "A", "A", "A"]],
    ["name3", 200, ["B", "A", "A", "C"]],
    ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]]
]

print(find_hack(array))
