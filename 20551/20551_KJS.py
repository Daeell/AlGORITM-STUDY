import sys

N, M = map(int, sys.stdin.readline().split())
A = []
nums = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A.sort()
for _ in range(M):
    nums.append(int(sys.stdin.readline()))


def BinarySearch(arr, target, s, e):
    while s <=e:
        m = (s+e) // 2
        if arr[m] == target:
            if arr[m-1] == target:
                e = m-1
            else:
                print(m)
                break

        elif arr[m] > target:
            s = m +1
        else:
            e = m -1


for i in range(M):
    if nums[i] in A:
        BinarySearch(A, nums[i],0, M-1)
    else:
        print(-1)

