import heapq

def solution(n, works):
    answer = 0

    heap = []
    for i in range(len(works)):
        heapq.heappush(heap, -works[i])

    for _ in range(n):
        x = -heapq.heappop(heap) -1
        if x <0:
            x =0
        heapq.heappush(heap,-x)
    
    while heap:
        num = -heapq.heappop(heap)
        answer += num*num

    
    return answer

print(solution(4,[4, 3, 3]))

# 효율성 X
# def solution(n, works):
#     answer = 0

#     cnt =1
#     while cnt<=n:
#         works.sort(reverse = True)
#         works[0]=works[0]-1
#         if works[0] <0:
#             works[0]=0
#         cnt+=1

#     for i in works:
#         answer +=i*i
    
#     return answer