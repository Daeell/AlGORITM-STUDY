# PASSED
from collections import deque
def solution(maps):
    answer = 0
    
    S, E, L = 0, 0, 0
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                S = (i,j)
            elif maps[i][j] == 'E':
                E = (i,j)
            elif maps[i][j] == 'L':
                L = (i,j)
    
    dr = (-1, 0, 0, 1)
    dc = (0, -1, 1, 0)
    visited = set()
    visited.add(S)
    queue = deque()
    queue.append((S[0], S[1], 0))
    while queue:
        r, c, cnt = queue.popleft()
        if (r,c) == L:
            answer = cnt
            break
        for i in range(4):
            r_ = r+dr[i]
            c_ = c+dc[i]
            if (r_,c_) not in visited and 0 <= r_ < len(maps) and 0 <= c_ < len(maps[0]):
                visited.add((r_,c_))
                if maps[r_][c_] != 'X':
                    queue.append((r_, c_, cnt+1))
    
    if answer == 0:
        return -1
    answer = 0
    
    visited = set()
    visited.add(L)
    queue = deque()
    queue.append((L[0], L[1], cnt))
    while queue:
        r, c, cnt = queue.popleft()
        if (r,c) == E:
            answer = cnt
            break
        for i in range(4):
            r_ = r+dr[i]
            c_ = c+dc[i]
            if (r_,c_) not in visited and 0 <= r_ < len(maps) and 0 <= c_ < len(maps[0]):
                visited.add((r_,c_))
                if maps[r_][c_] != 'X':
                    queue.append((r_, c_, cnt+1))
    
    if answer == 0:
        return -1
    
    return answer