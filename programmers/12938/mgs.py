def solution(n, s):
    
    if n > s :
        return [-1]
    
    num = [s//n for _ in range(n)]
    rem = s % n
    
    for i in range(rem) :
        num[i] += 1
    
    num.sort()
    
    return num
