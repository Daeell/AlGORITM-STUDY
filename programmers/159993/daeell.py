from collections import deque


def solution(maps):
    mr = len(maps)
    mc = len(maps[0])

    for i in range(mr):
        for j in range(mc):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)

    visited = [[False]*mc for _ in range(mr)]

    queue = deque(start[0], start[1], 0)
    visited[start[0]][start[1]] = True

    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == lever:
            break


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
