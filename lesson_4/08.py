"""
Отладка синтаксиса if/else
Во время разработки игры ваш партнёр Грег решил создать функцию для проверки того,
жив ли ещё пользователь, под названием checkAlive/ CheckAlive/ check_alive. К сожалению,
Грег допустил несколько ошибок при создании функции.
checkAlive// должен возвращать true CheckAlive, check_aliveе сли здоровье игрока больше 0,
или false, если оно равно 0 или ниже.
Функция получает один параметр health, который всегда будет целым числом от -10 до 10.
Link: https://www.codewars.com/kata/57089707fe2d01529f00024a
"""


def check_alive(health):
    return health > 0


print(check_alive(-4))
