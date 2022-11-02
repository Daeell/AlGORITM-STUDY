import sys
N= int(input())
# 상근이는 0, 창영이는 1
dp = [None for _ in range (N+1) ]
dp[1]= 0
dp[2]= 1
dp[3]= 0
dp[4]= 0
dp[5]= 0
dp[6]= 0

if (N>=7):
    for i in range(7, N+1) : 
        dp[i] = ~dp[i-1] & ~dp[i-3] & ~ dp[i-4]

if dp[N] == 0 :
    print("SK")
else :
    print("CY")

