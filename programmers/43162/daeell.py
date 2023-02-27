from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if visited[i] == False:
            bfs(i, n, computers, visited)
            answer += 1
    return answer


def bfs(start, n, computers, visited):
    q = deque([start])

    while q:
        conn = q.popleft()
        visited[conn] = True
        for i in range(n):
            if computers[conn][i] == 1 and visited[i] == False:
                q.append(i)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
