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

    visited = set()
    queue = deque([(start[0], start[1], 0, False)])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c, time, lever_on = queue.popleft()

        if (r, c) == end:
            return time
        if (r, c) in visited:
            continue

        visited.add((r, c))

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < mr and 0 <= nc < mc and maps[nr][nc] != 'X':

                if (nr, nc) == lever:
                    if not lever_on:
                        queue.append((nr, nc, time+1, True))
                    queue.append((nr, nc, time+1, lever_on))
                else:
                    queue.append((nr, nc, time+1, lever_on))

    return -1


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
