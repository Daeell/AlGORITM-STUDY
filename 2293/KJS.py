import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [0 for _ in range(k+1)]
dp[0] = 1
for coin in coins:
    for value in range(1,k+1):
        if value - coin >=0:
            dp[value] += dp[value-coin]

print(dp[k])
