#좌표 압축
import sys
input=sys.stdin.readline

N=int(input().strip())
A=list(map(int,input().strip().split()))

stad=min(A)


B=sorted(list(set(A)))


for i in range(N):
    print(B.index(A[i]),end=' ')