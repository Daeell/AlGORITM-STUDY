from collections import deque
# runtime error...
def solution(priorities, location):
    
    if len(priorities) == 1 :
        return 1
    
    answer = 0
    _print = deque()
    for i in range(len(priorities)) :
        _print.append([priorities[i], i])
    

    return_flag = False
    while return_flag == False :
        tmp = _print.popleft()
        _max = max(_print)

        if tmp[0] < _max[0] :
            _print.append(tmp)
            
        else :
            answer += 1
            if tmp[1] == location :
                return_flag = True


    return answer
