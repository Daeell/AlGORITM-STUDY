# 별 찍기 - 10
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def make_star(k):
    if k ==3:
        return ['***','* *','***']

    arr = make_star(k//3)
    answer_star = []
    
    for i in arr:
        answer_star.append(i*3)
    
    for i in arr:
        answer_star.append(i+' '*(k//3)+i)

    for i in arr:
        answer_star.append(i*3)
    
    return answer_star


N=int(input().strip())

print('\n'.join(make_star(N)))