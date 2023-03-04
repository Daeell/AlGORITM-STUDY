import heapq


def solution(n, s, a, b, fares):
    s -= 1
    a -= 1
    b -= 1
    graph = [[] for _ in range(n)]

    # 그래프 만들기
    for c, d, f in fares:
        c -= 1
        d -= 1
        graph[c].append((d, f))
        graph[d].append((c, f))

    # 각 지점에서 다른 지점까지의 최단 거리 구하기
    dist_s = dijkstra(s, graph)
    dist_a = dijkstra(a, graph)
    dist_b = dijkstra(b, graph)


INF = int(1e9)


def dijkstra(start, graph):
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, cur_node = heapq.heappop(heap)
        if dist[cur_node] < cost:
            continue
        for next_node, next_cost in graph[cur_node]:
            if cost + next_cost < dist[next_node]:
                dist[next_node] = cost + next_cost
                heapq.heappush(heap, (dist[next_node], next_node))

    return dist
