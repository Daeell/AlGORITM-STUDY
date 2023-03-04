import heapq
from collections import defaultdict

def solution(n, s, a, b, fares):
    answer = 100001*(len(fares))

    graph = defaultdict(set)
    for city1, city2, fee in fares:
        graph[city2].add((city1,fee))
        graph[city1].add((city2,fee))

    def dijkstra(start) :
        visited = [answer] * (n+1)
        visited[start]=0
        heap=[]
        heapq.heappush(heap,(0,start))

        while heap:
            cost_val, x =heapq.heappop(heap)
            
            if visited[x]<cost_val : continue
            
            for i in graph[x]:
                next=i[0]
                next_cost=cost_val+i[1]
                
                if next_cost<visited[next]:
                    visited[next]=next_cost
                    heapq.heappush(heap,(next_cost,next))
        
        return visited
    
    total_info = [[0]]
    for i in range(1,n+1):
        total_info.append(dijkstra(i))

    for i in range(1, n+1):
        answer = min(answer, total_info[s][i] + total_info[i][a] + total_info[i][b])

    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))