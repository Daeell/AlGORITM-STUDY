import sys
import math
# T = int(sys.stdin.readline())
# a, b = map(int, sys.stdin.readline().split())


# 1. 입력 받은 소수에서 한자리수만 바꾸어서 다른 소수를 내뱉는 함수 필요
# 2. 내뱉을 때 마다 원하는 소수가 아니면 또 들어가서 바꿈(1번 진행 될 때 마다 cnt 증가)
# 3. 하다가 불가능한 경우 Impossible 출력
# 4. 바꾸는 횟수가 최소값인 경우를 출력해야한다....


prime = [0] *(10000)

for i in range(2,10000):
    prime[i] = i


for i in range(2, int(math.sqrt(10000))+1):
    if prime[i] == 0:
        continue
    for j in range(i+i, 10000, i):
        prime[j] = 0

# 세자리수까지 다 0 으로 만든 뒤 set을 활용해 네자리 밑 소수는 제거
for i in range(1000):
    prime[i] = 0
prime_s = list(set(prime))
prime_s.remove(0)

# 딕셔너리 형태로 변환
prime_s_D = {i:list(str(prime_s[i])) for i in range(len(prime_s))}

def convert(A):
    A_S = list(str(A))
    available_prime = []
    
    for i in range(len(prime_s_D)):
        B= ''
        confirm = 0
        for j in range(4):
            if prime_s_D[i][j] == A_S[j]:
                confirm +=1
        
        if confirm == 3:
            for k in range(4):
                B += prime_s_D[i][k]
            
            A = int(B)
            
            available_prime.append(A)
    
    print(available_prime)
convert(1033)


