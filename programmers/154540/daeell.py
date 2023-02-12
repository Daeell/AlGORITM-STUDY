from collections import deque


def bfs(maps, visited, i, j, n, m):
    q = deque([(i, j)])
    visited[i][j] = 1
    s = int(maps[i][j])
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                q.append((nx, ny))
                visited[nx][ny] = 1
                s += int(maps[nx][ny])
    return s


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(maps, visited, i, j, n, m))
    if not answer:
        return [-1]
    answer.sort()
    return answer
