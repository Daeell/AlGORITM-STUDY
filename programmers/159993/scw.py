from collections import deque

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    
    for i in range(len(maps)):
        maps[i] = list(maps[i])
        if 'S' in maps[i]:
            idx = maps[i].index('S')
            start_point = [i, idx]
            
        if 'L' in maps[i]:
            idx = maps[i].index('L')
            Lever = [i, idx]
        if 'E' in maps[i]:
            idx = maps[i].index('E')
            end_point = [i, idx]

    def bfs(sp_y, sp_x, ep_y, ep_x):
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        dq = deque()
        dq.append((sp_y, sp_x))
        visited = [[-1]*n for _ in range(m)]
        visited[sp_y][sp_x]=0

        while dq:
            y, x = dq.popleft()
            if y == ep_y and x ==ep_x:
                return visited[y][x]

            for dy, dx in direction:
                ny = y + dy
                nx = x + dx
                if 0<=nx< n and 0<=ny<m and maps[ny][nx] !='X' and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x]+1
                    dq.append((ny,nx))
        
        return -1
    
    find_lever = bfs(start_point[0],start_point[1], Lever[0], Lever[1])
    find_end = bfs(Lever[0], Lever[1], end_point[0], end_point[1])

    if find_lever == -1 or find_end ==-1:
        answer = -1
    else:
        answer = find_lever + find_end

    return answer


print(solution(["SOOOOOL","XXXXXXO","OOOOOOO","OXXXXXX","OOOOOOE"]))