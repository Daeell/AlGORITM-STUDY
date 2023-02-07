from collections import deque

def solution(maps):
    answer = []
    graph = [[0] * len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        maps[i] = list(maps[i])
        
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        maps[x][y] = 'X'
        result = []
        result.append(maps[x][y])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= len(maps[0]) or ny < 0 or ny >= len(maps):
                    continue
                
                if maps[nx][ny] != 'X':
                    maps[nx][ny] == 'X'
                    result.append(maps[nx][ny])
        return result
                    
    for i in range(len(maps[0])):
        for j in range(len(maps)):
            if maps[i][j] != 'X':
                answer.append(bfs(i,j))
    
    
    
    return answer
