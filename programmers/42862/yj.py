def solution(n, lost, reserve):
    answer = 0
    
    n_lost = list(set(lost)- set(reserve)) # 잃어버리긴 했지만 여분이 있다면 빌릴 필요가 없음
    reserve = list(set(reserve)- set(lost)) #여분은 있지만 잃어버렷다면 빌려줄 수 없음 
    # print("lost", n_lost)
    # print("reserve",reserve)
    n_lost.sort()
    reserve.sort()
    
    for i in range(len(n_lost)):
        borrow = False
        if n_lost[i]-1 >0 :
            for j in range(len(reserve)):
                if reserve[j]== n_lost[i]-1 :
                    reserve[j] = -1 
                    borrow = True
                    break 
        if borrow : 
            answer +=1 
            continue 
        if n_lost[i]+1 <= n :
            for j in range(len(reserve)):
                if reserve[j]== n_lost[i]+1 :
                    reserve[j] = -1 
                    borrow = True
                    break            
        if borrow : 
            answer +=1 
    
    return answer + (n- len(n_lost))


print(solution(10, [3,9,10], [3,8,9]))