#k진수에서 소수 개수 구하기
import math

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

def convert(num, base):
    ret = ''
    while num>0:
        num, mod = divmod(num,base)
        ret += str(mod)
    return ret[::-1]

def solution(n, k):
    answer = 0
    temp_list = []
    temp = ''
    N = list(convert(n,k))
    
    for i in range (len(N)):
        if int(N[i]) !=0:
            temp+=N[i]
        elif int(N[i]) == 0:
            if len(temp)>0:
                temp_list.append(int(temp))
                temp=''
        
        if i == len(N)-1:
            if len(temp) >0:
                temp_list.append(int(temp))
                temp=''
    
    for i in temp_list:
        if is_prime_num(i) and i>1: 
            answer+=1

    return answer


print(solution(1000000, 10))

