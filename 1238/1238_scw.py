# 파티
import sys,heapq
from collections import defaultdict
input=sys.stdin.readline

n, m, x = map(int, input().strip().split()) # input : 도시 개수, 도로 정보, 목적지

graph = defaultdict(set)

for _ in range(m): # 도시와 도로 매핑해줌
    s,e,t = map(int, input().strip().split())
    graph[s].add((e,t))

def dijkstra(start) : # 다익스트라 탐색
    visited[start]=0
    heap=[]
    heapq.heappush(heap,(0,start)) # heap에는 시간, 시작점 순서로 넣어줌 - 시간이 가장 빠른애를 먼저 탐색할 수 있게함

    while heap:
        cost_val,x =heapq.heappop(heap)
        if visited[x]<cost_val : continue
        for i in graph[x]:
            next=i[0]
            next_cost=cost_val+i[1]
            if next_cost<visited[next]:
                visited[next]=next_cost
                heapq.heappush(heap,(next_cost,next))

answer=[0]*(n+1)
for i in range(1,n+1):
    visited = [999999999]*(n+1) # 방문 체크를 위한 visited
    dijkstra(i)
    if i == x: # 목적지에서 돌린 다익스트라는 각 도시로 돌아갈때의 최소 시간을 의미함
        for i in range(1,n+1):
            answer[i]=answer[i]+visited[i]
    else: # 출발지에서 목적지로 간 최소 시간
        answer[i]+=visited[x]


print(max(answer[1:n+1])) # 학생들 중 최대 소요시간 찾기 (0번은 자리 채우기였으니깐 빼고)