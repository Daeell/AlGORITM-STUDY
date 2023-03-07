#6 7 10 13 실패

import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while (scoville):
        x = heapq.heappop(scoville)
        if x>=K: 
            break
        elif len(scoville)==0 and x<K:
            answer = -1
            break

        y = heapq.heappop(scoville)

        temp = x+y*2
        answer +=1

        if temp<K or len(scoville) == 1:
            heapq.heappush(scoville, temp)
    
    return answer

print(solution([1,2,3], 5))