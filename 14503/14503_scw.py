#로봇 청소기
import sys
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
    graph[x][y]=2 # 방문처리 - 청소한 곳은 2로 표기
    flag = False # 만일 for문에 걸리지 않았다면 -> 청소를 이미 했거나 벽이었다면 Flase, 청소를 진행했으면 True
    for i in range(di-1,di-5,-1): # 탐색 방향 : 북 -> 서 -> 남 -> 동
        dir = i%4
        nx = x + direction[dir][0]
        ny = y + direction[dir][1]
        if graph[nx][ny] == 0:
            cnt+=1
            dfs(nx,ny,dir) # 한칸 이동 후 다시 탐색
            flag = True
            break # 이미 청소를 진행했으니 해당 for문은 버려도 됨
    if graph[x +direction[(di+2)%4][0]][y +direction[(di+2)%4][1]] != 1  and flag == False: # 벽이 아니라면
        dfs(x +direction[(di+2)%4][0],y +direction[(di+2)%4][1],di) # 뒤로 이동한다
    else:
        return
    

dfs(r,c,d) # 탐색 시작
print(cnt)