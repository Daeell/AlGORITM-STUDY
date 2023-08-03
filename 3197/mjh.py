import sys
from collections import deque
input = sys.stdin.readline

def water():
    while wq1:
        x, y = wq1.popleft()
        a[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or (nx, ny) in water_visited:
                continue
            if a[nx][ny] == '.':
                wq1.append((nx, ny))
            else:
                wq2.append((nx, ny))
            water_visited.add((nx, ny))

def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or (nx, ny) in swan_visited:
                continue
            if a[nx][ny] == '.':
                sq1.append((nx, ny))
            else:
                sq2.append((nx, ny))
            swan_visited.add((nx, ny))
    return False

ex, ey, ans = 0, 0, 0
dx, dy = (-1, 0, 0, 1), (0, -1, 1, 0)
R, C = map(int, input().split())
a = [list(input().strip()) for _ in range(R)]
water_visited = set()
swan_visited = set()
wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()

for i in range(R):
    for j in range(C):
        if a[i][j] == 'L':
            if not sq1:
                sq1.append((i, j))
                swan_visited.add((i, j))
            else:
                ex, ey = i, j
            a[i][j] = '.'

        if a[i][j] == '.':
            wq1.append((i, j))
            water_visited.add((i, j))

while True:
    water()
    if swan():
        break
    wq1 = wq2
    sq1 = sq2
    wq2 = deque()
    sq2 = deque()
    ans += 1

print(ans)