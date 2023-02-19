from collections import deque
def solution(maps):
    answer = 1
    N = len(maps)
    M = len(maps[0])
    
    
    def letsgo(x,y):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        q = deque()
        q.append((x,y))
        
        while q:
            x,y = q.popleft()            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < N and 0<= ny < M:
                    
                    if maps[nx][ny] == 0:
                        continue
                    
                    if maps[nx][ny] == 1:
                        maps[nx][ny] = maps[x][y] +1
                        q.append((nx,ny))
        return maps[N-1][M-1]
    answer = letsgo(0,0)
    if answer == 1:
        answer = -1
    return answer
