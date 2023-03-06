from collections import deque

def bfs(x, y, n, m, graph) :
    q = deque()
    q.append((x,y,0))
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q :
        x, y, cnt = q.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue

            if graph[nx][ny] != "X" and visited[nx][ny] == False and cnt < 2 :
                q.append((nx, ny, cnt+1))
                visited[nx][ny] = True
                if graph[nx][ny] == "P" :
                    return False
    return True

def solution(places):
    answer = []
    # print(places)
    for graph in places :
        return_flag = False
        n = len(graph)
        m = len(graph[0])
        for i in range(n) :
            for j in range(m) :
                if graph[i][j] == "P" :
                    if bfs(i, j, n, m, graph) == True :
                        pass
                    else :
                        return_flag = True
                        break
        if return_flag == True :
            answer.append(0)
        else :
            answer.append(1)
    return answer
