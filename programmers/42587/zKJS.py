def solution(priorities, location):
    answer = 0

    
    
    convert = []
    for index, priority in enumerate(priorities):
        convert.append((index,priority))
    while True:
        basic = convert.pop(0)
        if any(basic[1] < print[1] for print in convert):
            convert.append(basic)
        else:
            answer += 1
            if basic[0] == location:
                return answer
