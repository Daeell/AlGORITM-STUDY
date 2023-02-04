from collections import deque

def solution(s):
    answer = -1
    input_s=list(s)
    dq = deque()
    while(input_s):
        a=input_s.pop()
        if len(dq)==0:
            dq.append(a)
        elif len(dq)>0:
            if a == dq[-1]:
                dq.pop()
            else:
                dq.append(a)
    if len(dq)==0:
        answer = 1
    else:
        answer = 0
    return answer

print(solution('cdcd'))