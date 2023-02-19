import heapq
def solution(n, s, a, b, fares):
    answer = 20000001
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    for i in range(len(fares)):
        u, v, w = fares[i]
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    # dijkstra 함수는 각 노드에서 출발 했을 때 다른 노드로 갈 때의 최소값을 저장한 리스트를 반환
    def dijkstra(start):
        q = []
        distance = [INF] * (n+1)
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
        return distance
    
    all_case = [[]]
    # 1번부터 n노드 까지 각 노드에서 출발 했을 때 각 노드에 도착할때까지의 최소비용 저장
    for i in range(1,n+1):
        all_case.append(dijkstra(i))
    
    # 출발 노드에서 각 노드까지 합승을 진행해보고 그때 택시 비용의 총합 중 최소값을 반환
    for i in range(1,n+1):
        answer = min(answer, all_case[s][i] + all_case[i][a] + all_case[i][b])
    
    return answer
