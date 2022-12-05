#줄세우기
import sys
input=sys.stdin.readline

N = int(input().strip())

A=[]
for i in range(N):
    A.append(int(input().strip()))

# 최대 오름차순의 개수를 구하는 방법
dp=[0]*N

for i in range(N):
    for j in range(i):
        if A[i]>A[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1

print(N-max(dp))