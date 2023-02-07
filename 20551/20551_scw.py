# Sort 마스터 배지훈의 후계자   
import sys
input=sys.stdin.readline

N,M = map(int,input().strip().split())

# def find_index(mid):
#     while True:
#         if A[mid-1]==data and mid-1>=0:
#             mid=mid-1
#         else:
#             return mid

def BST(data,s,e):
    answer=0
    while s<=e :
        mid=(s+e)//2
        if A[mid]>=data:
            answer=mid
            e=mid-1            
        # elif A[mid] == data:
        #     answer=find_index(mid)
        #     break
        else:
            s=mid+1
        
    if A[answer] == data:
        print(answer)
    else:
        print(-1)

A=[]
for i in range(N):
    A.append(int(input().strip()))

A.sort()

for i in range(M):
    data=int(input().strip())
    s, e = 0, N-1
    BST(data,s,e)
