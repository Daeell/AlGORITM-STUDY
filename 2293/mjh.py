# PASSED

import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    coins = [int(input().strip()) for _ in range(N)]
    dp = [0]*(K+1)
    dp[0] = 1

    for i in range(N):
        for j in range(coins[i], K+1):
            dp[j] += dp[j-coins[i]]

    return dp[K]

print(main())