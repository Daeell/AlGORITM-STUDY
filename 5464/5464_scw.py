#주차장
import sys
from collections import deque
input=sys.stdin.readline

N,M = map(int, input().strip().split())

parking=[ int(input()) for _ in range(N)]
cars=[ int(input()) for _ in range(M)]
visited = [0]*N
answer=0
dq=deque()
for _ in range(2*M):
    dq.append(int(input().strip()))

while(dq != None):
    a=dq.popleft()
    if a>0:
        for i in range(N):
            if visited[i]==0:
                visited[i]=cars[a-1]
                answer +=parking[i]*cars[a-1]
                break
        if i==N-1:    
            dq.append(a) 
    else:
        for i in range(N):
            if visited[i]==cars[a*(-1)-1]:
                visited[i]=0
                break
    

print(answer)
                

