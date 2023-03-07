# PASSED

from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville[0] < K:
        a = heappop(scoville)
        if not scoville:
            heappush(scoville, a)
            break
        b = heappop(scoville)
        heappush(scoville, a + b*2)
        answer += 1
    
    return answer if scoville[0] >= K else -1