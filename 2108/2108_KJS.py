import sys

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()

print(round(sum(nums)/N))
print(nums[N//2])
print(max(nums, key=nums.count))  // 빈도수 큰것들중 제일 작은값 출력이라 답이 안됨

print(max(nums)-min(nums))
