def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 ==0:
            answer.append(num+1)
        else:
            a = num % 8
            if a == 1:
                answer.append(num+1)
            elif a == 3:
                answer.append(num+2)
            elif a == 5:
                answer.append(num+1)
            elif a == 7:
                answer.append(num+4)
            
    return answer
