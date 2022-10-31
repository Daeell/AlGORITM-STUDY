# Sort 마스터 배지훈의 후계자   
import sys

input=sys.stdin.readline

M,N = map(int,input().strip().split())

A=[]
for i in range(N):
    A.append(int(input().strip()))
A.sort()

D=[]
for i in range(M):
    D.append(int(input().strip()))


for data in D:
    s, e = 0, N-1
    while s<e :
        mid=(s+e)//2
        if A[mid]>=data:
            e=mid-1
        else:
            s=mid+1
    
    if e<0:
        e=0
        
    if A[(s+e)//2] !=data:
        print(-1)
    else:
        print((s+e)//2)

