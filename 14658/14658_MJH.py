from collections import deque
import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
N += 1; M += 1; L += 1

area = [[0]*(N) for _ in range(M)]

for _ in range(K):
    x, y = map(int, input().split())
    area[y][x] = 1

# begin find
maximum = 0
for x in range(N-L):
    line = deque()
    line_cnt = 0
    for y in range(M):
        if line_cnt == L:
            tmp = sum(line)
            if tmp > maximum:
                maximum = tmp
            line.popleft()
            line_cnt -= 1

        line.append(sum(area[y][x:x+L]))
        line_cnt += 1

print(K-maximum)

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
# [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
# [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]