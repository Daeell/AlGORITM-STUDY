def solution(board):
    N = len(board)
    end_point = (N-1, N-1)
    
    dx = (-1, 0, 0, 1)
    dy = (0, -1, 1, 0)
    
    visited = 1 << N**2
    arr = [0 for _ in range(visited)]
    
    def DFS(x, y, cost, direction, visited):
        if (x, y) == end_point:
            return cost
        
        if arr[visited]:
            return arr[visited]
        
        minimum = float('inf')
        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if 0 <= x_ < N and 0 <= y_ < N and board[x_][y_] != 1:
                if visited & 1 << (x_*N)+y_ == 0:
                    minimum = min(minimum, DFS(x_, y_, cost+100 if direction == i else cost+600, i, visited | 1 << (x_*N)+y_))
        
        arr[visited] = minimum
        return arr[visited]
    
    answer = DFS(0, 1, 100, 2, 1<<0 | 1<<1)
    answer = min(answer, DFS(1, 0, 100, 3, 1<<0 | 1<<N))
    
    return answer

# def solution(board):
#     N = len(board)
#     end_point = (N-1, N-1)
    
#     dx = (-1, 0, 0, 1)
#     dy = (0, -1, 1, 0)
    
#     visited = set()
#     visited.add((0,0))
#     def DFS(x, y, cost, direction):
#         if (x, y) == end_point:
#             return cost
        
#         minimum = float('inf')
#         for i in range(4):
#             x_ = x+dx[i]
#             y_ = y+dy[i]
#             if (x_,y_) not in visited and 0 <= x_ < N and 0 <= y_ < N and board[x_][y_] != 1:
#                 visited.add((x_,y_))
#                 minimum = min(minimum, DFS(x_, y_, cost+100 if direction == i else cost+600, i))
#                 visited.remove((x_,y_))
        
#         return minimum
    
#     visited.add((0,1))
#     answer = DFS(0, 1, 100, 2)
#     visited.remove((0,1))
#     visited.add((1,0))
#     answer = min(answer, DFS(1, 0, 100, 3))
    
#     return answer

# print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))