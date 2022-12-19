#가르침
import sys
from collections import deque
input=sys.stdin.readline

n, k = map(int, input().strip().split())

words=[]
for i in range(n):
    a=input().strip()
    words.append(list(a[4:len(a)-4]))

print(words)


if k<5 : 
    print(0)
elif k==5:
    print(n-len(words))
else:
    answer =0
    dq = deque()
    alp =[0]*25
    alp[ord('a')-97] =1
    alp[ord('c')-97] =1
    alp[ord('n')-97] =1
    alp[ord('t')-97] =1
    alp[ord('i')-97] =1
    for i in range(n):
        if 'a' in words[i]:
            words.remove('a')
        if 'c' in words[i]:
            words.remove('c')
        if 'n' in words[i]:
            words.remove('n')
        if 't' in words[i]:
            words.remove('t')
        if 'i' in words[i]:
            words.remove('i')        
        for j in range(len(words[i])):
            if alp[ord(words[i][j])-97] ==1:
                continue
            else:
                dq.append(words[i][j])
                alp[ord(words[i][j])-97] =1

    print(words)
    
    print(dq)
    alp =[0]*25
    alp[ord('a')-97] =1
    alp[ord('c')-97] =1
    alp[ord('n')-97] =1
    alp[ord('t')-97] =1
    alp[ord('i')-97] =1


