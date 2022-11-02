# 돌 게임 3
import sys
from collections import defaultdict
input=sys.stdin.readline

N= int(input().strip())
dp=defaultdict(set)

def find_winner(N):
    dp[0].add(True)
    dp[1].add(True)
    dp[2].add(False)
    dp[3].add(True)
    dp[4].add(True)

    for i in range(5, N+1):
        if(dp[i-1] == {False} or dp[i-3]=={False} or dp[i-4]== {False}):
            dp[i].add(True)
        else:
            dp[i].add(False)


find_winner(N)
if dp[N]=={True}:
    print('SK')
else:
    print('CY')