from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([i, p] for i, p in enumerate(priorities))

    while q:
        curr = q.popleft()
        for doc in q:
            if curr[1] < doc[1]:
                q.append(curr)
                break
        else:
            answer += 1
            if curr[0] == location:
                return answer


print(solution([2, 1, 3, 2], 2))
