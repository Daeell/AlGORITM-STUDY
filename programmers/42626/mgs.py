from heapq import *

def solution(scoville, K):
    answer = 0
    sco = []
    for val in scoville :
        heappush(sco, val)
    
    tmp = heappop(sco)
    if tmp >= K :
        return 0
    
    while sco and tmp < K :
        _next = heappop(sco)
        tmp = tmp + (_next * 2)
        heappush(sco, tmp)
        answer += 1
        tmp = heappop(sco)
    
    if tmp < K :
        return -1
        
    return answer
