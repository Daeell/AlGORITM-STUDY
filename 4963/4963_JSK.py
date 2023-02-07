import sys
from collections import deque

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]


def bfs(maps,a,b):  
    q = deque()
    maps[a][b] = 0
    q.append((a,b))

    while q:
        x,y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=h or ny<0 or ny>=w:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = 0
                q.append((nx,ny))
        

while True:
    w, h = map(int,sys.stdin.readline().split())
    maps = []
    if w == 0 and h ==0:
        break
    for _ in range(h):
        maps.append(list(map(int,sys.stdin.readline().split())))
    
    ans = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                bfs(maps,i,j)
                ans +=1
    
    print(ans)

