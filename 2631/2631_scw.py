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
        if A[i]>A[j] and dp[i]<dp[j]: # 이전 최대 길이를 복사할 기준 1. 현재 값보다 작으며 2. dp의 길이가 더 길때(최대길이 복사)
            dp[i]=dp[j]
    dp[i]+=1 # 자기 자신 추가

print(N-max(dp))