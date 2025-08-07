"""
Link: https://www.codewars.com/kata/62c93765cef6f10030dfa92b
"""


def solution(start, finish):
    difference = finish - start
    return (difference // 3) + (difference % 3)


print(solution(1, 5))
