N = int(input())
dp = [0] * (1001)
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 0
dp[4] = 0
dp[5] = 0
dp[6] = 0
for i in range(5,N+1):
    if dp[i-1] == 1 or dp[i-3] ==1 or dp[i-4] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[N] ==1:
    print('CY')
else:
    print('SK')
