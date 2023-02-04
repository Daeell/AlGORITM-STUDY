#소수경로
import sys
from collections import deque
input=sys.stdin.readline

def isPrime(a): # 에라토스테네스의 체
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

def bfs(s, cnt, e):
    s = list(str(s))
    cnt +=1
    for i in range (len(Primes)):
        str_cnt = 0
        temp = list(str(Primes[i]))
        for j in range(4):
            if s[j] == temp[j]:
                str_cnt +=1

        if str_cnt == 3:
            dq.append([Primes[i], cnt])
            Primes[i]=False
    
    while dq:
        num, cnt = dq.popleft()
        if num == e:
            return cnt
        cnt +=1
        num = list(str(num))
        for i in range (len(Primes)):
            temp_2 = list(str(Primes[i]))
            str_cnt = 0
            for j in range(4):
                if num[j] == temp_2[j]:
                    str_cnt +=1
            if str_cnt == 3:
                dq.append([Primes[i], cnt])
                Primes[i]=False
    
    return "Impossible"

N = int(input().strip())
cnt = 0
for i in range(N):
    s, e = map(int, input().strip().split())
    Primes = [] # 소수를 저장해놓을 리스트
    for i in range(1000, 9999):
        if(isPrime(i)):
            Primes.append(i)
    
    if s == e:
       print(0)
    else:
        dq = deque()
        print(bfs(s, 0, e))