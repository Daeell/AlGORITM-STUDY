import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    check_z = heapq.heappop(scoville)
    if check_z >= K:
        return answer
    else:
        heapq.heappush(scoville,check_z)
    while True:
        if len(scoville) == 1:
            break
        low1 = heapq.heappop(scoville)
        low2 = heapq.heappop(scoville)
        heapq.heappush(scoville, low1 + (low2)*2)
        answer += 1
        compare = heapq.heappop(scoville)
        if compare >= K:
            break
        else:
            heapq.heappush(scoville, compare)
    if len(scoville) == 1 and scoville[0] < K:
        answer = -1
        
    return answer
