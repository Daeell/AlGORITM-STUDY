def solution(n):
    answer_inv = ''
    while n:
        if (n % 3) !=0:
            answer_inv += str(n%3)
            n= n//3
        else:
            answer_inv += '4'
            n= n//3-1
    return answer_inv[::-1]
