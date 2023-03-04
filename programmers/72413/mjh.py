# PASSED
def solution(n, s, a, b, fares):
    s -= 1; a -= 1; b -= 1
    graph = [[100000000 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for fare in fares:
        v1, v2, w = fare
        v1 -= 1; v2 -= 1
        graph[v1][v2] = w
        graph[v2][v1] = w
    
    # Floyd-Warshall
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
        
    answer = graph[s][a] + graph[s][b]
    
    for i in range(n):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    
    return answer