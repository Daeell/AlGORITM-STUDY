import sys
n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [[0] * n for _ in range(2)]
dp[0][0] = numbers[0]
dp[1][0] = -1000
for i in range(1,n):
    dp[0][i] = max(numbers[i],dp[0][i-1] + numbers[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + numbers[i])

print(max(max(dp[0]),max(dp[1])))
