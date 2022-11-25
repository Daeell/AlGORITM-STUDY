import sys
input = sys.stdin.readline

N = int(input())    # N+1 일 이후 퇴사
works = [[0]*2 for _ in range(N)]

for i in range(N):
    works[i][0], works[i][1] = map(int, input().split())

dp = [0]*N

for d in range(1, N+1):
    for i in range(d):
        if i + works[i][0] < d+1:
            dp[d] += works[i][1]