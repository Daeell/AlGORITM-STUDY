# arrayA	       arrayB	        result
# [10, 17]	       [5, 20]	        0
# [10, 20]         [5, 17]	        10
# [14, 35, 119]	   [18, 30, 102]	7

import math 
def gcd(a, b) : # 단 a>b 여야 함 
    if (b==0) :
        return a; 
    else :
        return gcd(b, a%b)

def gcdArray(array) :
    num = len(array)
    if num==  0 :
        return 0 
    elif num== 1 :
        return array[0]
    else: 
        prev_gcd = gcd(array[0], array[1])
        if num >2 : 
            for i in range(2, len(array)-1) :
                prev_gcd = gcd(prev_gcd, array[i])
        return prev_gcd

def getDivisor(gcd) :
    if gcd == 1 :
        return [1]
    root = math.ceil(gcd**(1/2))
    divisor= [1, gcd] 
    for i in range(2, root) :
        if gcd % i  == 0 : # 나누어떨어진다
            divisor.append(i)
            divisor.append(gcd//i)
    return divisor


def solution(arrayA, arrayB):
    # 모든 숫자를 나눌 수 있는 -> 공약수 (유클리드호제법으로 최대 공약수를 구하면 그의 약수가 공약수들)
    # 공약수를 먼저 구하고, 이를 큰 수부터 순회하면서 다른 상대를 나눌 수 있는지 확인 

    arrayA.sort()
    arrayB.sort()
    
    prev_gcd_a = gcdArray(arrayA) # arrayA의 최대공약수
    prev_gcd_b = gcdArray(arrayB) # arrayB의 최대공약수
    
    a_divisor= getDivisor(prev_gcd_a)
    b_divisor= getDivisor(prev_gcd_b)
    a_divisor.sort(reverse=True)
    b_divisor.sort(reverse=True)
    # print("공약수 ", a_divisor, b_divisor)

    candidate = 0 
    # 내림차순 정렬을 햇는데, 첫 공약수가 1이라는 건 조건을 만족시킬 수 없다는 것
    if a_divisor[0] != 1 :    
        for i in range(len(a_divisor)):
            if a_divisor[i] not in b_divisor : 
                candidate = a_divisor[i]
                break
    if b_divisor[0] != 1 : 
        for i in range(len(b_divisor)):
            if b_divisor[i] <= candidate :
                break
            elif b_divisor[i] not in a_divisor : 
                candidate = b_divisor[i]
                break

    answer = candidate
    print(answer)
    return answer

print(solution([14, 35, 119], [18, 30, 102]))
print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
	 