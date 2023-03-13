import heapq


def solution(operations):
    max_heap = []
    min_heap = []
    for op in operations:
        i, j = op.split()
        if i == 'I':
            heapq.heappush(max_heap, -int(j))
            heapq.heappush(min_heap, int(j))
        elif i == 'D':
            if int(j) > 0 and max_heap:
                max_v = -heapq.heappop(max_heap)
                min_heap.remove(max_v)
            elif int(j) < 0 and min_heap:
                min_v = heapq.heappop(min_heap)
                max_heap.remove(-min_v)

    if len(max_heap) == 0:
        return [0, 0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]


print(solution(["I -45", "I 653", "D 1", "I -642",
      "I 45", "I 97", "D 1", "D -1", "I 333"]))
