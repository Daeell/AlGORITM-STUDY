import sys
import heapq
INF = 1e9
N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
# distance = [INF] * (N+1)

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

# print(graph)

def dijkstra(start,final):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    
    return distance[final]

ans = 0

for i in range(1,N+1):
    ans = max(ans,dijkstra(i,X) + dijkstra(X,i))

print(ans)
    
