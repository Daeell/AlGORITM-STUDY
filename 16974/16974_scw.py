import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

N, X =map(int,input().strip().split())

def recur(LEVEL):
    if LEVEL==0:
        return 'P'
    else:
        return 'B'+recur(LEVEL-1)+'P'+recur(LEVEL-1)+'B'

ham=recur(N)
cnt=0
print(len(ham), ham)
if X <len(ham):
    for i in range(X):
        if ham[i]=='P':
            cnt+=1
else:
    cnt += ham.count('P')
    for i in range(len(ham)-1,len(ham)-X-1,-1):
        if ham[i]=='P':
            cnt+=1           

print(cnt)
