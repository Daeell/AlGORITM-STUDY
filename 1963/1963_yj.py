import sys
from collections import deque
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline

# 네 자리 소수를 먼저 구하자
# 그리고 bfs + dp로 풀이하자 (bfs 여야 최소의 수를 찾을 수 있을 것)


a = [False,False] + [True]*(9999) # 배열 안에 False 두개와 그 이후 n-1개의 True가 있는 배열 
primes=set()

for i in range(2,10000):
  if a[i]:
    primes.add(i)
    for j in range(2*i, 10000, i):
        a[j] = False
# print(len(primes))

def bfs(a,b, cnt) :
    while True :
        visited.add(a)
        cnt = cnt + 1
        for i in range(0,4):
            for j in range(0, 10) :
                strA= str(a)
                str[i] = j
                intA = int(strA)
                if intA == b : 
                    break
                if intA in primes : 
                    if intA not in visited :
                      queue.append(intA)
        a = queue.popleft()
    

def doEach(a,b):
    visited = [] # visited 초기화 
    queue = deque()
    cnt = 0 ; 
    if a == b :
        return cnt
    deque.append(a)
    bfs(queue.popleft(), b, cnt) 
    print(cnt)

N= int(input())
for i in range(N) : 
    a, b = map(int, input().split())
    doEach(a,b)