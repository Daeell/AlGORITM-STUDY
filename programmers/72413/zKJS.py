import heapq
def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for i in range(len(fares)):
        u, v, w = fares[i]
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0,start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            
            if distance[now] < dist:
                continue
            
            for i in graph[now]:
                cost  = dist + i[1]
                
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
    dijkstra(s)
    print(distance[a],distance[b])
    
    return answer
