import sys
N = int(sys.stdin.readline())
idle = [0]
for _ in range(N):
    idle.append(int(sys.stdin.readline()))
# idle_sorted = sorted(idle)
dp = [1] * (N+1)

for i in range(1,N+1):
    for j in range(1,i):
        if idle[i] > idle[j]:
            dp[i] = max(dp[i],dp[j]+1)
            # print(dp[i])
# print(dp)

print(N-max(dp))
