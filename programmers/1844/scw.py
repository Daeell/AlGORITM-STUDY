# BFS pass
from collections import deque

def solution(maps):
    answer = 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    M = len(maps)
    N = len(maps[0])
    visited = [[-1]*N for _ in range(M)]
    dq=deque()
    dq.append([0,0])
    visited[0][0] =1
    while dq:
        i, j= dq.popleft()

        for dy, dx in direction:
            nx = j + dx
            ny = i + dy

            if 0<=nx<N and 0<=ny<M and maps[ny][nx] ==1 and visited[ny][nx] ==-1:
                visited[ny][nx] = visited[i][j] +1
                dq.append([ny,nx])

    answer = visited[M-1][N-1]
    
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))


# DFS 7 9 11 13, 효율성 1,3 런타임에러, 2,4 실패

# answer = 0

# def solution(maps):
#     global answer
#     direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

#     M = len(maps)
#     N = len(maps[0])
#     answer = N*M+1

#     def dfs(y,x, cnt):
#         global answer
        
#         if maps[y][x]==1:
#             maps[y][x] = 0
#             cnt +=1
        
#         if y == M-1 and x ==N-1:
#             answer = min(answer, cnt)
        
#         for dy, dx in direction:
#             ny = y + dy
#             nx = x + dx
#             if 0<=nx<N and 0<=ny<M and maps[ny][nx] ==1:
#                 dfs(ny, nx, cnt)
#         return

#     dfs(0,0, 0)

#     if answer == N*M+1:
#         answer = -1

#     return answer