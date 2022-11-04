# 게임을 만든 동준이
import sys
input=sys.stdin.readline

def find_score():
    N=int(input().strip())
    A=[]
    for _ in range(N):
        A.append(int(input().strip()))

    answer =0
    for idx in range(N-1,0,-1):
        if A[idx]<=A[idx-1]:
            answer+= A[idx-1]-A[idx]+1
            A[idx-1]=A[idx]-1
        idx=idx-1
    return answer

print(find_score())
