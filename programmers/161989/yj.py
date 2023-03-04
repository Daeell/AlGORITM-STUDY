def solution(n, m, section):
    if m== 1 :
        return len(section)
    
    # 어디까지 페인트칠이 되었는지 표시하는 변수
    covered = 0
    answer = 0
    for i in range(len(section)):
        if section[i] > covered :
            covered = section[i] + (m-1)
            answer +=1 
        if covered >= n :
            break 

    return answer
    
print(solution(8, 4, [2, 3, 6]))  #2 
