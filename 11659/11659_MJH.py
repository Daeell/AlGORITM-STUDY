import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_arr = list(map(int, input().split()))

# added_arr[i]에는 num_arr[0]~[i-1]까지의 합이 저장되어 있음.
added_arr = [0]*(N+1)
for i in range(1, N+1):
    added_arr[i] = added_arr[i-1] + num_arr[i-1]

# test case만큼 반복
for _ in range(M):
    left, right = map(int, input().split())

    print(added_arr[right] - added_arr[left-1])