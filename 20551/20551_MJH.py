import sys

def binary_search(val, start, end):
    answer = 0

    while start <= end:
        mid = (start+end)//2
        if sorted_arr[mid] < val:
            start = mid+1
        else:
            answer = mid
            end = mid-1

    if sorted_arr[answer] == num:
        return answer
    else: return -1

input = sys.stdin.readline
N, M = map(int, input().split())
original_arr = [0]*N
sorted_arr = [0]*N
for i in range(N):
    original_arr[i] = int(input().strip())

sorted_arr = sorted(original_arr)

for i in range(M):
    num = int(input().strip())
    print(binary_search(num, 0, N-1))
