# 아직 못 품
def solution(board):
    global minimum
    end_point = (len(board)-1, len(board[0])-1)
    minimum = float('inf')
    dx = (-1, 0, 0, 1)
    dy = (0, -1, 1, 0)
    
    def DFS(x, y, cost, direction):
        global minimum
        if (x, y) == end_point:
            minimum = min(cost, minimum)
            return
        
        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            minim = float('inf')
            if (x_,y_) not in visited and 0 <= x_ < len(board) and 0 <= y_ < len(board[0]):
                if board[x_][y_] != 1:
                    DFS(x_, y_, cost+100 if direction == i else cost+600, i)
    
    return minimum