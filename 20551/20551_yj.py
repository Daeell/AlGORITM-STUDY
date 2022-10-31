import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N,M = map(int, input().split())
seq = []

for i in range(N):
    seq.append(int(input()))
seq.sort()

def answer(D,N) :
    # D를 이분탐색으로 seq 에서 찾으면 된다
    left = 0 
    right = N-1 
    while left<right : 
        mid = (left+right)//2
        if D <= seq[mid] :
            right = mid 
        else : # D> seq_b[mid] 
            left = mid +1
    if left == right :
        if D == seq[left] :
            print(left)
            return 
        else :
            print(-1)
            return 
    else :
        print(-1)
        return 

for i in range(M):
    D = int(input())
    answer(D, N)

