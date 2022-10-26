import sys
from collections import deque

graph = []
for _ in range(5):
    graph.append(list(map(int, sys.stdin.readline().split())))
print(graph)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = []

for i in range(5):
    for j in range(5):

        def dfs(i, j):
            nums = deque([])
            nums.append((a, b))
            res.append(graph[a][b])
            count = 0

            while count != 5:
                x, y = nums.pop()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                if graph[x][y]
