import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

edges=[]
result = 0
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost,a,b))

edges.sort()

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for edge in edges:
    cost, a, b = edge;
    if find_parent(parent,a) != find_parent(parent,b):
        union(parent, a,b)
        print(parent)
        result += cost
print(result)
