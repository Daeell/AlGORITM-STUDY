import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(input())
graph = [[]for _ in range(V+1)]
INF = 1e9
distance = [INF] * (V+1)
for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))


def djkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
djkstra(K)
for i in range(1,V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
