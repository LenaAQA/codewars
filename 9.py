# Вы — судья на конкурсе по еде, и вам нужно выбрать победителя!
#
# В конкурсе участвуют три вида блюд, и каждый из них оценивается по разному.
# Баллы начисляются следующим образом:
#
# Куриные крылышки: 5 баллов
#
# Гамбургеры: 3 очка
#
# Хот-доги: 2 балла
#
# Напишите функцию, которая поможет вам создать табло.
# В качестве параметра она принимает список объектов, представляющих участников, например:
# Он должен возвращать свойства «имя» и «оценка», отсортированные по оценке;
# если оценки равны, сортировать в алфавитном порядке по имени.


def scoreboard(who_ate_what):
    d = []
    for i in who_ate_what:
        score = i.get("chickenwings", 0) * 5 + i.get("hamburgers", 0) * 3 + i.get("hotdogs", 0) * 2
        d.append({"name": i["name"], "score": score})
    return sorted(d, key=lambda x: (-x["score"], x["name"]))


print(scoreboard([{"name": "Billy The Beast", "chickenwings": 17, "hamburgers": 7, "hotdogs": 8},
                  {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
                  {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},
                  {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]))
