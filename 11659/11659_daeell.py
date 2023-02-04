import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    nums[i] = nums[i - 1] + nums[i]
# [0, 5, 9, 12, 14, 15] - store cumulative sum

for _ in range(m):
    s, e = map(int, input().split())
    # start elem, end elem
    sum_ = nums[e] - nums[s-1]
    # if you want to get elem[2] to elem[4]
    # nums[4] = nums[1] + nums[2] + nums[3] + nums[4]
    # nums[1] = nums[1]
    # nums[4] - nums[1] = nums[4] + nums[3] + nums[2]

print(nums)
