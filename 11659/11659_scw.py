#구간 합 구하기 4
#import sys
#input=sys.stdin.readline

def solve():
    N,M=map(int,input().split())
    Nums=tuple(map(int,input().split()))

    for _ in range (M):
        sum1=0
        s,e=map(int,input().split())
        for i in range(s-1,e):
            sum1+=Nums[i]
        print(sum1)

solve()