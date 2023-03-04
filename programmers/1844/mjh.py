# PASSED
from collections import deque

def solution(maps):
    dx = (1, 0, 0, -1)
    dy = (0, -1, 1, 0)
    queue = deque()
    visited = set()
    queue.append((0,0,1))
    flag = False

    while queue:
        x, y, cnt = queue.popleft()

        if x == len(maps)-1 and y == len(maps[0])-1:
            flag = True
            break

        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if (x_, y_) not in visited and 0 <= x_ < len(maps) and 0 <= y_ < len(maps[0]):
                if maps[x_][y_] == 1:
                    queue.append((x_, y_, cnt+1))
    
    return cnt if flag == True else -1