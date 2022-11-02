N = int(input())
DP = [-1]*(1001)
DP[1] = 1
DP[2] = 0
DP[3] = 1
DP[4] = 1

if N > 4:
    for i in range(5, N+1):
        DP[i] = (min(DP[i-1], DP[i-3], DP[i-4])+1)%2

if DP[N] == 0:
    print("CY")
else: print("SK")