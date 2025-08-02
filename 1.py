# Кто-то взломал счёт. Запись каждого ученика представлена в виде массива.
# Объекты в массиве представлены в виде массива оценок для каждого имени и общего балла.


def find_hack(arr):
    res = []
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
            res.append(name)
    return res


array = [
  ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
  ["name2", 110, ["B", "A", "A", "A"]],
  ["name3", 200, ["B", "A", "A", "C"]],
  ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]]
]
print(find_hack(array))
