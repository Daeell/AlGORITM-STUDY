# 장장 3일만에 풀었다...
from heapq import heappush, heappop
def solution(board):
    answer = float('inf')
    N = len(board)
    
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    dp = [[[-1 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = 0
    dp[0][0][1] = 0

    queue = []
    heappush(queue, (0, 0, 0))

    while (queue):
        cost, x, y = heappop(queue)
        if x == N-1 and y == N-1:
            answer = min(answer, cost)
            continue

        for i in range(4):
            xi = x+dx[i]
            yi = y+dy[i]
            if 0 <= xi < N and 0 <= yi < N and board[xi][yi] != 1:
                minimum = float('inf')
                for j in range(4):
                    if dp[x][y][j] != -1:
                        tmp = dp[x][y][j]+100 if i == j else dp[x][y][j]+600
                        if tmp < minimum:
                            minimum = tmp
                if dp[xi][yi][i] == -1 or dp[xi][yi][i] != -1 and dp[xi][yi][i] > minimum:
                    dp[xi][yi][i] = minimum
                    heappush(queue, (minimum, xi, yi))

    return answer





# from heapq import heappush, heappop
# def solution(board):
#     N = len(board)
#     end_point = (N-1, N-1)
    
#     dx = (-1, 0, 0, 1)
#     dy = (0, -1, 1, 0)
    
#     arr = set()

#     queue = []
#     if board[0][1] == 0:
#         heappush(queue, (100, 0, 1, 2, 1<<0 | 1<<1))
#     if board[1][0] == 0:
#         heappush(queue, (100, 1, 0, 3, 1<<0 | 1<<N))
#     while (queue):
#         cost, x, y, direction, visited = heappop(queue)
#         if (x, y) == end_point:
#             break

#         for i in range(4):
#             x_ = x+dx[i]
#             y_ = y+dy[i]
#             if 0 <= x_ < N and 0 <= y_ < N and board[x_][y_] != 1:
#                 visited_ = visited | 1 << (x_*N)+y_
#                 if visited_ not in arr and visited & 1 << (x_*N)+y_ == 0:
#                     arr.add(visited_)
#                     heappush(queue, (cost+100 if direction == i else cost+600, x_, y_, i, visited | 1 << (x_*N)+y_))
    
#     return cost





# def solution(board):
#     N = len(board)
#     end_point = (N-1, N-1)
    
#     dx = (-1, 0, 0, 1)
#     dy = (0, -1, 1, 0)
    
#     arr = dict()
    
#     def DFS(x, y, cost, direction, visited):
#         if (x, y) == end_point:
#             return cost
        
#         if visited in arr:
#             return arr[visited]
        
#         minimum = float('inf')
#         for i in range(4):
#             x_ = x+dx[i]
#             y_ = y+dy[i]
#             if 0 <= x_ < N and 0 <= y_ < N and board[x_][y_] != 1:
#                 if visited & 1 << (x_*N)+y_ == 0:
#                     minimum = min(minimum, DFS(x_, y_, cost+100 if direction == i else cost+600, i, visited | 1 << (x_*N)+y_))
        
#         arr[visited] = minimum
#         return arr[visited]
    
#     answer = DFS(0, 1, 100, 2, 1<<0 | 1<<1)
#     answer = min(answer, DFS(1, 0, 100, 3, 1<<0 | 1<<N))
    
#     return answer





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
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))