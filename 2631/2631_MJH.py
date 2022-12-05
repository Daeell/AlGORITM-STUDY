import sys
input = sys.stdin.readline

N = int(input().strip())
input_ = [input().strip() for _ in range(N)]
start_state = "".join(input_)
end_state = "".join([str(i) for i in range(1, N+1)])

orderset = set()
orderset.add(start_state)

cur = start_state
for i in range(0, N):
    n = cur[i]
    rest = cur[0:i-1] + cur[i:N]
    print(n, rest)