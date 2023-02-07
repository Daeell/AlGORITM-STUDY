#구간 합 구하기 4
import sys
input=sys.stdin.readline

def solve():
    N,M=map(int,input().strip().split())
    Nums=tuple(map(int,input().strip().split()))

    arr=[0]*N
    arr[0]=Nums[0]
    for k in range (1,N):
        arr[k]=arr[k-1]+Nums[k]
    
    for _ in range (M):
        s,e=map(int,input().strip().split())

        if s-1 ==0:
            print(arr[e-1])
        elif s-1 == e-1:
            print(Nums[e-1])
        else:
            print(arr[e-1]-arr[s-2])

solve()