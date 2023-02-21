from collections import deque
def solution(maps):
    answer = 0
    graph = []
    for i in range(len(maps)):
        graph.append(list(maps[i]))
    N = len(graph)
    M = len(graph[0])
    start = []
    end = []
    lever = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'S':
                start.append((i,j))
                graph[i][j] ='O'
            elif graph[i][j] == 'L':
                lever.append((i,j))
                graph[i][j] ='O'
            elif graph[i][j] == 'E':
                end.append((i,j))
                graph[i][j] ='O'
    def bfs(x,y,N,M,resN,resM):
        cnt = 0
        q = deque()
        visited = [[0] * M for _ in range(N)]
        visited[x][y] = 1
        q.append((x,y))
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        while q:
            x,y = q.popleft()
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny <M and graph[nx][ny] =='O':
                    if visited[nx][ny] != 0:
                        continue
                    if graph[nx][ny] =='O':
                        visited[nx][ny] += visited[x][y] + 1
                        q.append((nx,ny))
        return visited[resN][resM] -1
    if bfs(start[0][0],start[0][1],N,M,lever[0][0],lever[0][1]) == -1 or bfs(lever[0][0],lever[0][1],N,M,end[0][0],end[0][1]) == -1:
        answer = -1
    else:
        answer = bfs(start[0][0],start[0][1],N,M,lever[0][0],lever[0][1]) + bfs(lever[0][0],lever[0][1],N,M,end[0][0],end[0][1])
    return answer
