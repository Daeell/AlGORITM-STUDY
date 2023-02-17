# PASSED
from heapq import heappush, heappop
def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    
    heapworks = []
    for work in works:
        heappush(heapworks, -work)
    
    while n:
        tmp = heappop(heapworks)
        tmp += 1
        n -= 1
        heappush(heapworks, tmp)
    
    for work in heapworks:
        answer += (-work)**2
    
    return answer