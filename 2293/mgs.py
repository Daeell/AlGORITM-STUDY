n, k = map(int, input().split())
# print(n,k)

coin = []
for _ in range(n) :
    coin.append(int(input()))
# print(coin)

dp = [0] * (k+1)
dp[0] = 1
for money in coin :
    for i in range(1, k+1) :
        if i >= money :
            dp[i] += dp[i-money]
print(dp[k])
