N,K=map(int,input().split())

if(N>=K):
    print(N-K)
    exit()

dp=list(0 for _ in range(K+1))

for i in range(N):
    dp[i]=N-i

for i in range(N+1,K+1):
    if(i%2==0):
        dp[i]=min(dp[i-1]+1,dp[i//2]+1)
    else:
        dp[i]=min(dp[i-1]+1,dp[(i+1)//2]+2)

print(dp[K])