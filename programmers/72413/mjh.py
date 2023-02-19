# 푸는 중
from collections import defaultdict
from heapq import heappush, heappop

def lowest_fare(graph, a, b):
    fare = 0
    heap = []
    visited = set()
    
    
    for e in graph[a]:
        heappush(heap, e)
        
    while heap:
        w, v = heappop(heap)
        visited.add(v)
        fare += w
        if v == b:
            return fare
        for e in graph[v]:
            if e[1] not in visited:
                heappush(heap, e)
    
def solution(n, s, a, b, fares):
    answer = 0
    graph = defaultdict(list)
    for fare in fares:
        v1, v2, w = fare
        graph[v1].append((w, v2))
        graph[v2].append((w, v1))
    
    print(lowest_fare(graph, s, a))
    
    return answer