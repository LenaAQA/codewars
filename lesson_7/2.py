"""
Link: https://www.codewars.com/kata/571d2e9eeed4a150d30011e7
"""


def scoreboard(who_ate_what):
    new_list = []
    for i in who_ate_what:
        score = i.get("chickenwings", 0) * 5 + i.get("hamburgers", 0) * 3 + i.get("hotdogs", 0) * 2
        new_list.append({"name": i["name"], "score": score})
    return sorted(new_list, key=lambda x: (-x["score"], x["name"]))


print(scoreboard([{"name": "Billy The Beast", "chickenwings": 17, "hamburgers": 7, "hotdogs": 8},
                  {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
                  {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},
                  {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]))
