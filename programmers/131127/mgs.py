from collections import deque

def solution(want, number, discount):
    answer = 0
    _dict = dict(zip(want, number))
    
    # 답지 만들어 놓기
    for item in discount :
        if item not in _dict :
            _dict[item] = 0
    
    # 비교 답지 만들기
    cpr_dict = dict()
    for key in _dict.keys() :
        cpr_dict[key] = 0
    # print(cpr_dict)
    check_list = []
    discount = deque(discount)

    while discount :
        _next = discount.popleft()

        if sum(cpr_dict.values()) < sum(number) :
            cpr_dict[_next] += 1
            check_list.append(_next)
        else :
            cpr_dict[_next] += 1
            cpr_dict[check_list[0]] -= 1
            del check_list[0]
            check_list.append(_next)
        
        if cpr_dict == _dict :
            answer += 1
            
    return answer
