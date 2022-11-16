import sys

N, M = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().split()))

# def myway_sum(s,e):
#     ans = 0
#     for i in range(s,e+1):
#         ans += nums[i]
#     return ans

nums_sum = [0] * (N+1)
for i in range(0,N+1):
    nums_sum[i] = nums_sum[i-1] + nums[i]
for i in range(M):
    s, e = map(int,sys.stdin.readline().split())
    if s == e:
        print(nums[e])
    else:
        print(nums_sum[e]-nums_sum[s-1])
