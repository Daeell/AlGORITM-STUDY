#시간초과

from collections import deque
def solution(board):
    answer = 0
    N = len(board)

    def bfs(y,x,cost):
        dq = deque()
        directiton = [(0,1),(1,0),(0,-1),(-1,0)]

        board[0][0] = 0
        for dy, dx in directiton:
            ny = y + dy
            nx = x + dx
            if 0<=nx<N and 0<=ny<N and board[ny][nx] ==0:
                if abs(ny-y)==1:
                    cost = 100
                    dq.append((ny,nx,True,cost))
                if abs(nx - x) ==1:
                    cost = 100
                    dq.append((ny,nx,False, cost))
        
        while dq:
            i, j, vertical, cur_cost = dq.popleft()
            if board[i][j] == 0:
                board[i][j] = cur_cost
            else:
                board[i][j] = min(board[i][j], cur_cost)
            
            for k in range(4):
                ny = i + directiton[k][0]
                nx = j + directiton[k][1]
                if 0<=nx<N and 0<=ny<N:
                    if abs(ny-i)==1 and vertical == True:
                        cost = cur_cost+100
                        if board[ny][nx] ==0:
                            dq.append((ny,nx,True,cost))
                        elif cost < board[ny][nx]:
                            dq.append((ny,nx,True,cost))
                    
                    elif abs(ny-i)==1 and vertical == False:
                        cost = cur_cost+600
                        if board[ny][nx] ==0:
                            dq.append((ny,nx,True,cost))
                        elif cost < board[ny][nx]:
                            dq.append((ny,nx,True,cost))
                    
                    elif abs(nx - j) ==1 and vertical == False:
                        cost = cur_cost+100
                        if board[ny][nx] ==0:
                            dq.append((ny,nx,False,cost))
                        elif cost < board[ny][nx]:
                            dq.append((ny,nx,False,cost))
                    
                    elif abs(nx - j) ==1 and vertical == True:
                        cost = cur_cost+600
                        if board[ny][nx] ==0:
                            dq.append((ny,nx,False,cost))
                        elif cost < board[ny][nx]:
                            dq.append((ny,nx,False,cost))

    bfs(0,0,0)
    answer = board[N-1][N-1]
    return answer

print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))