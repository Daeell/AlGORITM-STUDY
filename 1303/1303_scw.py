#전쟁-전투
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

N, M = map(int, input().strip().split())

graph = []
for i in range(M):
    graph.append(list(input().strip()))

direction = [(1,0), (-1,0), (0,-1), (0,1)]

def dfs(r,c,s):
    global TEMP
    if graph[r][c]==s:
        TEMP +=1
        graph[r][c] = 1

    for x, y in direction:
        nx = r + x
        ny = c + y
        if 0<= nx < M and 0 <= ny < N :
            if graph[nx][ny] == s:
                dfs(nx,ny,s)
    return
    
ANSWER_A=0
ANSWER_B=0
for i in range(M):
    for j in range(N):
        TEMP=0
        if 0<= i < M and 0 <= j < N :
            if graph[i][j] == 'W':
                dfs(i,j,'W')
                ANSWER_A += TEMP*TEMP
            elif graph[i][j] == 'B':
                dfs(i,j,'B')
                ANSWER_B += TEMP*TEMP
    
print(ANSWER_A, ANSWER_B)