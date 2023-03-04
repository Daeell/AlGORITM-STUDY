def solution(w,h):
    answer = 1
    
    def gcd(a,b):
        while b>0:
            a, b = b, a%b
        return a
    
    answer = w*h - (w+h - gcd(w,h))

    return answer


print(solution(8,12))