#숫자 카드
import sys
from bisect import bisect_left
input=sys.stdin.readline

N= int(input().strip())

A = list(map(int,input().strip().split()))
A.sort()
M= int(input().strip())

B = list(map(int,input().strip().split()))
for i in B:
    idx =bisect_left(A,i)
    if idx > len(A)-1:
        print(0, end=' ')         
    elif A[idx] == i:
        print(1, end=' ')
    else:
        print(0, end=' ')