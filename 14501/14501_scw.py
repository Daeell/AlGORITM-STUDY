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
answer=[0 for _ in range(N+1)]
answer[end] = money 
# print(answer)
for i in range(N):
    if A[i][0] == end and A[i][2]>money:
        end = A[i][0]
        money = A[i][2]
        # print(end, money)
        answer[end]=money
    elif A[i][1]>= end and A[i][0]<=N:
        end = A[i][0]
        money = A[i][2]
        # print(end, money)
        answer[end]=money
    elif A[i][0]==N+1 and A[i][1]>=end:
        money = A[i][2]
        answer[end]+=money
    
    if i>=A[0][0]:
        answer[i+1] = answer[i]+answer[i+1]

print(answer[N])
