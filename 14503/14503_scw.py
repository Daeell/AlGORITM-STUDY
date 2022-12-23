#로봇 청소기
import sys
from collections import deque
input=sys.stdin.readline

n,m = map(int,input().strip().split())

r,c,d = map(int,input().strip().split())

direction = [(-1,0), (0,1), (1,0), (0,-1)] # 북, 동, 남, 서


graph=[]
for i in range(n):
    graph.append(list(map(int,input().strip().split())))

cnt =1

def dfs (x,y,di):
    global cnt
    graph[x][y]=2
    for i in range(di,di+4):
        dir = i-1
        nx = x + direction[(dir)%4][0]
        ny = y + direction[(dir)%4][1]
        if graph[nx][ny] == 0:
            cnt+=1
            dfs(nx,ny,dir)
            break
        if graph[x +direction[(dir+2)%4][0]][y +direction[(dir+2)%4][0]]==2 and i==di+3:
            dfs(x +direction[(dir+2)%4][0],y +direction[(dir+2)%4][0],dir)
    

print(graph)
dfs(r,c,d)
print(cnt)