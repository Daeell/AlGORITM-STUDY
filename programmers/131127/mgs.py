from collections import deque

def solution(want, number, discount):
    answer = 0
    _sum = sum(number)
    _dict = dict(zip(want, number))
    
    tmp = dict()
    _deque = deque()
    for i in range(_sum) :
        if discount[i] in tmp :
            tmp[discount[i]] += 1
        else :
            tmp[discount[i]] = 1
        _deque.append(discount[i])

    if tmp == _dict :
        answer += 1

    cnt = 0
    discount = discount[_sum:]

    while cnt != len(discount)-1 :
        _del = _deque.popleft()
        tmp[_del] -= 1

        
        if discount[cnt] in tmp :
            tmp[discount[cnt]] += 1
        else :
            tmp[discount[cnt]] = 1

        if tmp == _dict :
            answer += 1

        cnt += 1

    return answer

solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])
