import sys
from collections import deque

c, r = map(int,sys.stdin.readline().split())
maps = []
for _ in range(r):
    maps.append(list(map(int,sys.stdin.readline().split())))

visited =[[False]* c for _ in range(r)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

res=[]
def bfs(x,y):
    q = deque([])
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < c and 0<= ny < r:
                continue
            
            if maps[nx][ny] == 0:
                

bfs(0,0)
print(visited)
