#좌표 압축
import sys
from collections import defaultdict
input=sys.stdin.readline

N=int(input().strip())
A=list(map(int,input().strip().split()))

B=sorted(A)

dic = defaultdict(list)
cnt=0
for i in range(N):
    if not(dic[B[i]]):        
        dic[B[i]].append(cnt)
        cnt+=1

for i in range(N):
    print(dic[A[i]][0],end=' ')