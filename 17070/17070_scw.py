#파이프 옮기기 1
import sys
input=sys.stdin.readline

N=int(input().strip())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().strip().split())))

print(graph)

visited=[[-1]*N for _ in range(N)]
print(visited)


graph[0][0] =-1
graph[0][1] =-1

direct1 = [[0,1],[1,1]] # 가로
direct2 = [[1,1],[1,0]] # 세로
direct3 = [[1,0],[1,1],[0,1]] # 대각선

def dfs(x,y,nx,ny):
    bf = [x,y]
    cur = [nx,ny]

    if cur[0] - bf[0] == 0 and cur[1] - bf[1] == 1: # 가로
        for dx, dy in direct1:
            nx = cur[0] + dx
            ny = cur[1] + dy
            if 0 <= nx < N  and 0 <= ny < N:
                if graph[nx][ny] != 1 :
                    graph[nx][ny] -=1
                    bf[0] = cur[0]
                    bf[1] = cur[1]
                    cur[0] = nx
                    cur[1] = ny
                    dfs(bf[0], bf[1], cur[0], cur[1])
            elif nx == N and ny == N:
                return
    elif cur[0] - bf[0] == 1 and cur[1] - bf[1] == 0: # 세로
        for dx, dy in direct1:
            nx = cur[0] + dx
            ny = cur[1] + dy
            if 0 <= nx < N  and 0 <= ny < N:
                if graph[nx][ny] != 1 :
                    graph[nx][ny] -=1
                    bf[0] = cur[0]
                    bf[1] = cur[1]
                    cur[0] = nx
                    cur[1] = ny
                    dfs(bf[0],bf[1],cur[0],cur[1])
            elif nx == N and ny == N:
                return

    elif cur[0] - bf[0] == 1 and cur[1] - bf[1] == 1: # 대각선
        for dx, dy in direct1:
            nx = cur[0] + dx
            ny = cur[1] + dy
            if 0 <= nx < N  and 0 <= ny < N:
                if graph[nx][ny] != 1 :
                    graph[nx][ny] -=1
                    bf[0] = cur[0]
                    bf[1] = cur[1]
                    cur[0] = nx
                    cur[1] = ny
                    dfs(bf[0],bf[1],cur[0],cur[1])
            elif nx == N and ny == N:
                return

dfs(0,0,0,1)
