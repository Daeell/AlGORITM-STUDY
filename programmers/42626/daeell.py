from heapq import heappop, heappush, heapify


def solution(scoville, K):
    sc = scoville
    heapify(sc)

    answer = 0
    while sc[0] < K:
        if len(sc) == 1:
            return -1
        fir = heappop(sc)
        sec = heappop(sc)
        new = fir + sec*2
        heappush(sc, new)
        answer += 1
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
