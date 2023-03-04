def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 ==0:
            answer.append(num+1)
        else:
            num_bin ='0'+bin(num)[2:]
            for i in range(-1,-len(num_bin)-1,-1):
                if num_bin[i] == '0':
                    answer.append(num+2**(abs(i)-2))
                    break
            
    return answer
