# Improved performance.
# 86236KB, 528ms -> 72144KB, 384ms
#
# Changed methods :
#   - heappop & heappush -> heapreplace
#   - sort by [0] and [1] -> only [0] (no sorting options)

from heapq import heappush, heapreplace
import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    lecList = []
    for i in range(N):
        lecList.append(list(map(int, input().split())))

    lecList.sort()

    heap = []
    heappush(heap, lecList[0][1])

    for i in range(1, N):
        if heap[0] <= lecList[i][0]:
            heapreplace(heap, lecList[i][1])
        else:
            heappush(heap, lecList[i][1])
    
    return len(heap)

print(sol())