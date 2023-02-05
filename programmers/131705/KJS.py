import itertools
def solution(number):
    answer = 0
    total = list(itertools.combinations(number,3))
    for three in total:
        if sum(three) == 0:
            answer+=1
    return answer
