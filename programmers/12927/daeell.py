import heapq


def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)
    while n > 0:
        if works[0] == 0:
            break
        work = heapq.heappop(works)
        work += 1
        heapq.heappush(works, work)
        n -= 1
    return sum([work ** 2 for work in works])


print(solution(4, [4, 3, 3]))

# def solution(n, works):
#     works = sorted(works, reverse=True)
#     answer = 0
#     while n > 0:
#         if works[0] == 0:
#             break
#         works[0] -= 1
#         works = sorted(works, reverse=True)
#         n -= 1
#     for work in works:
#         answer += work ** 2
#     return answer
