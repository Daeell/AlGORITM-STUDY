def solution(n, lost, reserve):
    lost_dup = set(lost) - set(reserve)
    reserve_dup = set(reserve)-set(lost)
    reserve.sort()
    answer = n - len(lost_dup)
    for loose in lost_dup:
        if loose-1 in reserve_dup:
            reserve_dup.remove(loose-1)
            answer +=1
        elif loose+1 in reserve_dup:
            reserve_dup.remove(loose+1)
            answer +=1
    
    return answer
