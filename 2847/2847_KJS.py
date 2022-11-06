import sys

N = int(sys.stdin.readline())
nums=[]
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
cnt = 0
nums.reverse()
for i in range(N-1):
    if nums[i] <= nums[i+1]:
        cnt += nums[i+1]-nums[i]+1
        nums[i+1] = nums[i]-1
    else:
        continue

print(cnt)
