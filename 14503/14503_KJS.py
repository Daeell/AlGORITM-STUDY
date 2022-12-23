import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

maps = []
visited = [[0] * M for _ in range(N)]
print(visited)
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 1. 현재 위치를 청소한다
visited[r][c] = 1
cnt = 1


# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다
def bfs(r,c,d):
    que = deque()
    # visited[r][c] = 1
    que.append((r,c))

    while que:
        r, c = que.popleft()

        
