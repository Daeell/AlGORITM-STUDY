#퇴사
import sys
from collections import defaultdict
input=sys.stdin.readline

N=int(input().strip())

A=[]
for i in range(N):
    end, money = map(int,input().strip().split())
    A.append([end+i+1,i+1,money]) #end, start, money

A.sort()
print(A)

end = A[0][0]
money = A[0][2]

for i in range(N):
    if A[i][0] == end and A[i][2]>money:
        end = A[i][0]
        money = A[i][2]
        print(end, money)
    elif A[i][1]>= end and A[i][0]<=N:
        end = A[i][0]
        money = A[i][2]
        print(end, money)

