def solution(arrayA, arrayB):

    def GCD(a, b):
        if a%b == 0:
            return b
        else:
            return GCD(b, a%b)

    answer = 0

    a = arrayA[0]
    for i in range(1, len(arrayA)):
        a = GCD(a, arrayA[i])
    
    flag = True
    for i in range(len(arrayB)):
        if arrayB[i]%a == 0:
            flag = False
            break
    
    if flag == True:
        answer = a

    b = arrayB[0]
    for i in range(1, len(arrayB)):
        b = GCD(b, arrayB[i])
    
    flag = True
    for i in range(len(arrayA)):
        if arrayA[i]%b == 0:
            flag = False
            break
    
    if flag == True:
        answer = max(answer, b)

    return answer

print(solution([14, 35, 119], [18, 30, 102]))