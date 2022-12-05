import sys
input = sys.stdin.readline

N = int(input().strip())
init_state = [int(input().strip()) for _ in range(N)]

dp_table = [0]*N

for i in range(N-1, -1, -1):
    max_incr = 0

    for j in range(i+1, N):
        if init_state[i] < init_state[j] and max_incr < dp_table[j]:
            max_incr = dp_table[j]

    dp_table[i] = max_incr + 1

print(N - max(dp_table))