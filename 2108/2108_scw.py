#통계학

import sys
from collections import defaultdict
input = sys.stdin.readline

N=int(input().strip())

A=[]
dic=defaultdict(list)
sum_num=0
mini=4001
maxi=-4001
for _ in range(N):
    k=int(input().strip())
    sum_num+=k
    A.append(k)
    mini=min(mini,k)
    maxi=max(maxi,k)
    dic[k].append(1)
    

aver=round(sum_num/N)
print(aver)
A.sort()
print(A[N//2])

temp=[]
for i in dic:
    if temp==[]:
        temp.append([i,len(dic[i])])
    elif len(dic[i])>temp[0][1]:
        temp=[]
        temp.append([i,len(dic[i])])
    elif len(dic[i])==temp[0][1]:
        temp.append([i,len(dic[i])])


temp.sort(key=lambda x:x[0])
if len(temp)>=2:
    print(temp[1][0])
else:
    print(temp[0][0])
print(maxi-mini)