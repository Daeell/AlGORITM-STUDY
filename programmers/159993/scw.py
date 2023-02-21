from collections import deque

def solution(maps):
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    dq = deque()
    m = len(maps)
    n = len(maps[0])
    visited = [[-1]*n for _ in range(m)]
    for i in range(len(maps)):
        maps[i] = list(maps[i])
        if 'S' in maps[i]:
            idx = maps[i].index('S')
            dq.append((i, idx))
            maps[i][idx] = 0
            visited[i][idx]=0
        if 'L' in maps[i]:
            idx = maps[i].index('L')
            Lever = [i,idx]
        if 'E' in maps[i]:
            idx = maps[i].index('E')
            end_point = [i,idx]

    def bfs(end_point_y, end_point_x)
        while dq:
            y, x = dq.popleft()
            if y == end_point[0] and x ==end_point[1]:
                break

            for dy, dx in direction:
                ny = y + dy
                nx = x + dx
                if 0<=nx< n and 0<=ny<m and maps[ny][nx] !='X' and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x]+1
                    dq.append((ny,nx))
    

    return visited[temp[0]][temp[1]]


print(solution(["SOOOXS","OOXXOO","OOOEOX","OOOXXX","OOOXXX"]))