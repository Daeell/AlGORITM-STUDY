from collections import deque

def solution(maps):
    answer = []
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    dq = deque()
    
    def bfs(x,y,TEMP):
        dq.append((x,y))
        
        while dq:
            x, y =dq.popleft()
            
            for dx, dy in direction:
                nx = x+dx
                ny = y+dy
                if 0<=nx<len(maps) and 0<=ny< len(maps[0]):
                    if maps[nx][ny] !='X' and maps[nx][ny] != '-1':
                        TEMP += int(maps[nx][ny])
                        maps[nx][ny] = '-1'
                        dq.append((nx,ny))
        return TEMP

    for i in range(len(maps)):
        maps[i] = list(maps[i])                    
        
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] !='X' and maps[i][j] !='-1':
                TEMP =int(maps[i][j])
                maps[i][j] = '-1'
                answer.append(bfs(i,j,TEMP))
    
    if len(answer) ==0:
        answer=[-1]
        return answer
    else:
        answer.sort()
        return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))