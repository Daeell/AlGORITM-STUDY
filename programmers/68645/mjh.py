# PASSED
import sys
sys.setrecursionlimit(6000)

def solution(n):
    global p, num
    p = 0
    num = 1

    answer = []

    arr = [[0 for _ in range(i)] for i in range(1, n+1)]

    def recur(depth, MAX_DEPTH):
        global p, num
        if depth == MAX_DEPTH:
            for i in range(p, len(arr[depth])-p):
                arr[depth][i] = num
                num += 1
            return
        
        arr[depth][p] = num
        num += 1
        recur(depth+1, MAX_DEPTH)
        if arr[depth][-(p+1)] == 0:
            arr[depth][-(p+1)] = num
            num += 1
    
    magic_number = 0
    while magic_number*2 <= n-(magic_number+1):
        recur(magic_number*2, n-(magic_number+1))
        p += 1
        magic_number += 1

    for i in range(len(arr)):
        answer.extend(arr[i])

    return answer

print(solution(6))