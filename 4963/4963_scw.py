#섬의 개수
import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**6)


while True: # 입력의 끝이 정해져 있지 않으므로 계속 받기위한 while
    try:
        N,M=map(int,input().strip().split())
        A=[]
        direction = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)] # 상하좌우 대각선까지 가능하니깐
        visited=[[-1]*N for _ in range(M)] # 방문체크
        for _ in range(M):
            A.append(list(map(int,input().strip().split()))) # 지도 정보 받아주고
        cnt=0 # 섬 개수 카운트

        def dfs(x,y): # dfs 함수
            for dx, dy in direction:
                nx=x+dx
                ny=y+dy
                if 0<=nx<M and 0<=ny<N and A[nx][ny]==1 and visited[nx][ny]==-1:
                    visited[nx][ny]=1
                    dfs(nx,ny)
        
        for i in range(M): # 섬이 끊어지면 다음 섬을 찾아야하니깐
            for j in range(N):
                if visited[i][j]==-1 and A[i][j]==1:
                    visited[i][j]=1
                    cnt+=1
                    dfs(i,j)
        
        if N==0 and M==0: # 지도가 아예 없으면 그냥 패스
            continue
        else: # 그게 아니면 print
            print(cnt)

    except ValueError: # 더이상 input이 없으면 break
        break
