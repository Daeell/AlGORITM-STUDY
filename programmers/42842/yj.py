import math

def solution(brown, yellow):
    
    # 가로 길이가 w, 세로가 h일 때, brown = w*2 + h*2 -4, yellow = (w-2)(h-2)
    
    a = -1
    b = 2+ brown/2
    c = -brown -yellow

    # 해가 2개인 경우
    if b**2 - 4*a*c > 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
    
    # 해가 1개인 경우
    elif b**2 - 4*a*c == 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
        x2 = x1
    

    answer = [] #가로, 세로 
    if x1>x2 : 
        answer.append(round(x1))
        answer.append(round(x2))
    else:
        answer.append(round(x2))
        answer.append(round(x1))
        
    return answer


