from heapq import *

def solution(n, works):
    answer = 0
    if sum(works) <= n :
        return 0
    
    work = []
    for time in works :
        heappush(work, [-time, time])
    
    while n != 0 :
        tmp = heappop(work)[1]
        tmp -= 1
        heappush(work, [-tmp, tmp])
        n -= 1
    
    for time in work :
        tmp = time[1]
        answer += tmp**2
    return answer
