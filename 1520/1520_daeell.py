import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(m)]
visited = [['no'] * n for _ in range(m)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def dfs(row, col):
    if row == m-1 and col == n-1:
        visited[row][col] = '도착'
        return 1
    if visited[row][col] != 'no':
        return visited[row][col]
    visited[row][col] = 0

    for i in range(4):
        new_row = row + dx[i]
        new_col = col + dy[i]
        if 0 <= new_row < m and 0 <= new_col < n and map_[new_row][new_col] < map_[row][col]:
            visited[row][col] += dfs(new_row, new_col)
        # 방문을 안했고, 길이 있으면 이전에 경로만큼 더해준다.
    return visited[row][col]


dfs(0, 0)

print(visited)
print(visited[0][0])
