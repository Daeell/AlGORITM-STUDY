import heapq
def solution(operations):
    answer = []
    heap = []
    for i in range(len(operations)):
        if operations[i].split()[0] == 'I':
            heapq.heappush(heap, int(operations[i].split()[1]))
            # print(heap)
        else:
            if int(operations[i].split()[1]) == -1 and len(heap) != 0:
                heapq.heappop(heap)
            elif int(operations[i].split()[1]) == 1 and len(heap) != 0:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
    if len(heap) == 0:
        answer = [0,0]
    else:
        answer = [max(heap), min(heap)]
                
                
    return answer
