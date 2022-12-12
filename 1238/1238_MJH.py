import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    N, M, X = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        w, v, t = map(int, input().split())
        graph[w].append((v, t))

    # i == 출발점
    for i in range(N):
        if i == X:
            continue

        visited = set()
        arr = [101]*(N+1)
        
        for node in graph:
            for way in graph[node]:
                if way[1] 
    
    # for print graph. (test)
    # for i in graph:
    #     print(graph[i])


main()