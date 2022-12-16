# 가장 긴 증가하는 부분 수열 2
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

N = int(input().strip())

A = list(map(int,input().strip().split()))

dp=[0]*(N)
dp_idx=0

def binary_search(s,e,value):
    mid = (s+e)//2
    
    if s>e:
        return -1
    if dp[mid]<= value <dp[mid+1]:
        return mid
    if dp[mid] >=value:
        return binary_search(s,mid-1,value)
    if dp[mid] <value:
        return binary_search(mid+1, e, value)

for i in range(N):
    if A[i] < dp[0]:
        idx =0
    else:
        idx = binary_search(0,dp_idx,A[i])

    if idx == -1:
        dp[dp_idx] = A[i]
        dp_idx +=1
    else:
        dp[idx] = A[i]

print(dp_idx)