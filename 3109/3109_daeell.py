import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def dfs_recursive(sr, sc):
    visited.add((sr, sc))

    if sr == r:
        cnt += 1
        return

    for go in gogo:
        if 0 <= sr+go <= r and graph[sr+go][sc+1] != 'x' and (sr+go, sc+1) not in visited:
            dfs_recursive(sr+go, sc+1)
    return


r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
cnt = 0
gogo = [-1, 0, 1]
visited = set()
for row in range(r):
    dfs_recursive(row, 0)

print(cnt)
