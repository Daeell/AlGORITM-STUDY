import sys
from collections import defaultdict
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
N = int(input())
graph = defaultdict(set)
for i in range(-1, N):
    graph[i]= set()

arr = list(map(int, input().split()))
delnode = int(input())
for i in range(N): 
    graph[arr[i]].add(i) # 부모 노드에 나를 추가 

visited = set()

def dfs(node, visited) :
    visited.add(node)
    for i in graph[node] :
        if i not in visited:
            dfs(i, visited)

dfs(delnode, visited)

for i in range(N): 
    if i in visited :  # 내가 삭제 노드라면 
        if graph.get(arr[i], False) : 
            graph[arr[i]].remove(i)
        del graph[i]

ans = 0
for k, v in graph.items():
    if k == -1 :
        continue 
    if len(v)== 0 :
        ans+=1 

print(ans)
