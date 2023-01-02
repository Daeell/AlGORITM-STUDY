#석판 자르기
import sys, copy
from collections import deque
input=sys.stdin.readline


N = int(input().strip())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip().split())))

dq = deque()

def find_dirty():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                dq.append([j,i])
find_dirty()
temp=[]
while dq:
    x,y = dq.popleft()
    if 2 == len(set(list(zip(*graph))[x])) and 2 ==len(set(graph[y])): # 양방향
        temp.append([x,y,0])
        continue
    elif 2 == len(set(list(zip(*graph))[x])): # 세로
        temp.append([x,y,1])
        continue
    elif 2 ==len(set(graph[y])): # 가로
        temp.append([x,y,2])
        continue
    temp.append([x,y,3])

temp.sort(key=lambda x:x[2])
print(temp)
visited = copy.deepcopy(graph)

flag=True

if len(temp) ==0:
    print(-1)
else:
    for x,y,d in temp:
        if d ==0: # 양방향
            for i in range(x,N): # 가로 커팅
                visited[y][i] = -1
            for j in range(x,-1,-1):
                visited[y][j] = -1
        else:
            if flag == True:
                for i in range(x,N): # 가로 커팅
                    if graph[y][i]==0 and visited[y][i]==0:
                        visited[y][i] = -1
                    elif graph[y][i]==2 or graph[y][i]==1:
                        flag = False
                        break
                for j in range(x,-1,-1):
                    if graph[y][i]==0 and visited[y][i]==0:
                        visited[y][i] = -1
                    elif graph[y][i]==2 or graph[y][i]==1:
                        flag = False
                        break
            if flag == False:
                for i in range(y,N): # 세로 커팅
                    if graph[i][x]==0 and visited[i][x]==0:
                        visited[i][x] = -1
                    elif graph[i][x]==2 or graph[i][x]==1:
                        flag = True
                        break
                for j in range(x,-1,-1):
                    if graph[i][x]==0 and visited[i][x]==0:
                        visited[i][x] = -1
                    elif graph[i][x]==2 or graph[i][x]==1:
                        flag = True
                        break


print(visited)

