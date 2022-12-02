from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
lecList = []
for i in range(N):
    lecList.append(list(map(int, input().split())))

lecList.sort(key=lambda x: (x[0], x[1]))

heap = []
heappush(heap, lecList[0][1])

for i in range(1, N):
    if heap[0] <= lecList[i][0]:
        heappop(heap)
    heappush(heap, lecList[i][1])

print(len(heap))