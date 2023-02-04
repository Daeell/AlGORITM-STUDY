import sys
sys.stdin = open('python/input.txt', 'r')
input = sys.stdin.readline


# 부모노드를 찾는다 (사이클 여부를 확인하기 위해)
def find_parent(parent, node):
    if parent[node] == node:
        return node
    else:
        parent[node] = find_parent(parent, parent[node])
        return parent[node]


# 그래프를 연결한다.
def union(parent, nodeA, nodeB):
    parentNodeA = parent[nodeA]
    parentNodeB = parent[nodeB]

    if parentNodeA < parentNodeB:
        parent[nodeB] = parentNodeA
    else:
        parent[nodeA] = parentNodeB


def main():
    N = int(input())
    M = int(input())
    parent = [i for i in range(N+1)]
    graph = []

    for _ in range(M):
        startNode, endNode, weight = map(int, input().split())
        graph.append([startNode, endNode, weight])

    graph = sorted(graph, key=lambda x: x[2])

    answer = 0

    for startNode, endNode, weight in graph:
        startNodeRoot = find_parent(parent, startNode)
        endNodeRoot = find_parent(parent, endNode)

        if startNodeRoot != endNodeRoot:
            union(parent, startNodeRoot, endNodeRoot)
            answer += weight

    print(answer)


main()
