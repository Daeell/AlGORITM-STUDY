from collections import deque
import copy

def solution(n, lost, reserve):
    
    answer = 0

    total_list = []
    lost_2 = copy.deepcopy(lost)
    lost = set(lost) - set(reserve)
    reserve = set(reserve) - set(lost_2)

    answer = n - len(lost)
    
    for i in range(1,n+1):
        if i in lost:
            total_list.append([i, 0])
        elif i in reserve:
            total_list.append([i, 1])

    
    total_list.sort(key=lambda x:(x[0]))

    dq = deque(total_list)

    while dq:
        num, check = dq.popleft()
        if len(dq)>0 and dq[0][0] == num+1 and check + dq[0][1] ==1:
            dq.popleft()
            answer+=1

            
    return answer


print(solution(5,[1,3,5],[2,4,5]))