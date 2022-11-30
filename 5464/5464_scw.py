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
wait=deque()
for _ in range(2*M):
    dq.append(int(input().strip()))

while(len(dq)!=0 or len(wait) !=0):
    a=dq.popleft()
    if a>0:
        for i in range(N):
            if visited[i]==0:
                visited[i]=a
                answer +=parking[i]*cars[a-1]
                break
            if i==N-1:
                wait.append(a)
    else:
        i = visited.index(abs(a))
        visited[i]=0
        if len(wait) !=0:
            b=wait.popleft()
            visited[i]=b
            answer+=parking[i]*cars[b-1]

print(answer)
