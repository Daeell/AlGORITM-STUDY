from itertools import combinations
def solution(number):
    answer = 0     
    for item in list(combinations(number, 3)) :
        a,b,c = item[0], item[1], item[2]
        if a+b+c == 0  :
            answer += 1
    return answer
