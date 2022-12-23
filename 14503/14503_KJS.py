import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

maps = []
visited = [[0] * M for _ in range(N)]
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 1. 현재 위치를 청소한다
visited[r][c] = 1
cnt = 1


# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다
while 1:
    flag = 0
    
    # 4방향을 도는데 왼쪽방향으로 돌 수 있게 설정한다
    for _ in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]

        # 한번 왼쪽으로 방향이 바뀌었으면 실행

        d = (d+3)%4

        if 0<= nx < N and 0<= ny <M and maps[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt +=1
                r = nx
                c = ny
                flag = 1
                break

    if flag ==0:
        if maps[r-dx[d]][c-dy[d]] == 1:  # 탐색을 진행하였는데 사방이 모두 벽인 경우
            print(cnt)
            break
        else:
            r,c = r-dx[d], c -dy[d] # 벽이 아니면 후진을 진행해주고 다시 while문 상단으로 올라간다
