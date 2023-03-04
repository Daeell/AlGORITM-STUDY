def check_num(n):
    final_point = 0
    for i in range(1,n+1):
        final_point+=i
    
    return final_point

def solution(n):
    answer = []
    temp = [[0 for _ in range(i)] for i in range(1, n+1)]

    final_point = check_num(n)

    i=0 # top -> bottom
    j=0 # left -> right
    cnt =1 # start value

    while True:
        while True: # top --> bottom
            if i>=len(temp) or j>=len(temp) or temp[i][j] !=0:
                break
            temp[i][j] = cnt
            cnt +=1
            i+=1
            if i>= len(temp) or temp[i][j] !=0:
                i -=1
                j +=1
                break
        
        while True: # left --> right
            if i>=len(temp) or j>=len(temp) or temp[i][j] !=0:
                break
            temp[i][j] = cnt
            cnt +=1
            j +=1
            if j>= len(temp) or temp[i][j] !=0:
                i -=1
                j -=2
                break
        
        while True: # bottom --> top
            if i>=len(temp) or j>=len(temp) or temp[i][j] !=0:
                break
            temp[i][j] = cnt
            cnt +=1
            i -=1
            j -=1
            if temp[i][j] !=0:
                i +=2
                j +=1
                break
        
        if cnt == final_point +1:
            break
    
    for i in temp:
        answer += i
    
            
    return answer

print(solution(4))