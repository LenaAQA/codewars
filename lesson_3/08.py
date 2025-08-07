"""
Бобу нужен быстрый способ вычисления объема прямоугольного параллелепипеда
с использованием трех величин: length, width и height параллелепипеда.
Напишите функцию, которая поможет Бобу с этим вычислением.
Link: https://www.codewars.com/kata/58261acb22be6e2ed800003a
"""


def get_volume_of_cuboid(length, width, height):
    return length * width * height


print(get_volume_of_cuboid(1, 2, 2))
