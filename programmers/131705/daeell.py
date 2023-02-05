from itertools import combinations


def solution(number):
    combis = list(combinations(number, 3))
    answer = 0
    for combi in combis:
        if sum(combi) == 0:
            answer += 1
    return answer
