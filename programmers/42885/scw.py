#구명보트

from collections import deque

def solution(people, limit):
    answer = 0

    people.sort()

    dq = deque(people)
    while dq:
        if dq[0] + dq[-1] <= limit:
            dq.popleft()
                
        if dq:
            dq.pop()
        answer+=1

    return answer

print(solution([70, 50, 80, 50], 100))