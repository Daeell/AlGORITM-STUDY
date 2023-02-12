from collections import deque

def BFS(arr, x, y, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if (x, y) not in visited:
            visited.add((x, y))
            cnt += int(arr[x][y])
            for i in range(4):
                cx = x + dx[i]
                cy = y + dy[i]
                if 0 <= cx < len(arr) and 0 <= cy < len(arr[0]):
                    if arr[cx][cy] != 'X':
                        queue.append((cx, cy))

    return cnt, visited

def solution(maps):
    answer = []

    arr = []
    for line in maps:
        arr.append([*line])

    visited = set()

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if (i, j) not in visited:
                if arr[i][j] != 'X':
                    cnt, visited = BFS(arr, i, j, visited)
                    answer.append(cnt)

    return sorted(answer) if answer != [] else [-1]

print(solution(["111", "XXX", "111"]))