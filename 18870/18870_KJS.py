import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
zip = list(set(nums))
count =[]


for i in range(N):
    cnt = 0
    for j in range(len(zip)):
        if nums[i] > zip[j]:
            cnt +=1
    count.append(cnt)        

print(count)
