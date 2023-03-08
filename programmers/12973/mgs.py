def solution(s):

    stack = []
    
    for val in s :
        if stack :
            if stack[-1] == val :
                stack.pop()
            else :
                stack.append(val)
        else :
            stack.append(val)
            
    if stack : 
        return 0
    else :
        return 1
