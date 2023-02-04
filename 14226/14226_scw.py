#이모티콘
import sys
from collections import deque
input=sys.stdin.readline

N = int(input().strip())

emo = 1
clipboard = 0
visited = dict()
visited[(1, 0)] = 0

def bfs(emo, clipboard):
    dq=deque()
    dq.append((emo, clipboard))

    while dq:
        emo, clipboard = dq.popleft()
        
        if emo == N: # 이모티콘 개수에 도달했으면
            return visited[(emo, clipboard)]
        
        if (emo, emo) not in visited.keys(): # 현재 이모티콘 개수를 clipboard에 복사
            visited[(emo, emo)] = visited[(emo, clipboard)] + 1
            dq.append((emo, emo))
        
        if (emo + clipboard, clipboard) not in visited.keys(): # clipboard에 있는 걸 화면으로 복사
            visited[(emo + clipboard, clipboard)] = visited[(emo, clipboard)] +1
            dq.append((emo + clipboard, clipboard))
        
        if (emo -1, clipboard) not in visited.keys(): # 이모티콘 개수 -1
            visited[(emo -1, clipboard)] = visited[(emo, clipboard)] +1
            dq.append((emo -1, clipboard))
    

print(bfs(emo, clipboard))
