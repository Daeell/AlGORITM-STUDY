#소수 경로
import sys
from collections import deque
input=sys.stdin.readline

N= int(input().strip())

def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

def checking_status(start, mid):
    cnt = 0
    start = list(str(start))
    mid = list(str(mid))
    for i in range(4):
        if start[i] == mid[i]:
            cnt +=1
        else:
            continue
    if cnt ==3:
        return True
    else:
        return False
        
dq = deque()

for _ in range(N):
    start, end = map(int, input().strip().split())
    answer_list = []
    answer_mid_list = []
    for i in range(start,end+1):
        if(isPrime(i)):
            if(checking_status(start, i)):
                dq.append(i)
            answer_list.append(i)

    print(answer_list)
    print(answer_mid_list)

