from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    queue = deque()
    queue.append((0, 0, 1))

    visited = set()
    visited.add((0, 0))

    while queue:
        r, c, count = queue.popleft()

        if r == n-1 and c == m-1:
            return count

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, count+1))

    return -1
