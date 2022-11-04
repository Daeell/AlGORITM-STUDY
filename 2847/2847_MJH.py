import sys

N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = int(sys.stdin.readline().strip())

count = 0

for i in range(N-1, 0, -1):
    if arr[i-1] - arr[i] >= 0:
        count += arr[i-1] - (arr[i] - 1)
        arr[i-1] = arr[i] - 1

print(count)