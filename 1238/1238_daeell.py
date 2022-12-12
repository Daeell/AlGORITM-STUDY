import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n)]
cost = [[101] * (n+1) for _ in range(n + 1)]
for i in range(n):
    cost[i][i] = 0

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s-1].append([e-1, t])


def bfs(s):
    queue = deque([])
    queue.append(s)
    while (queue):
        start = queue.popleft()
        for i in (graph[start]):
            # 최소 경로가 아니라면...다시 방문을 하는 것입니다.
            if (cost[s][i[0]] > cost[s][start] + i[1]):
                queue.append(i[0])
                cost[s][i[0]] = min(cost[s][i[0]], cost[s][start] + i[1])


for i in range(n):
    bfs(i)

answer = 0
for i in range(n):
    temp = cost[i][s]
    answer = max(answer, temp)

print(answer)

print(graph)
print(cost)
