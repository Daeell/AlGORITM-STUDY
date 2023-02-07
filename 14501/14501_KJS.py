import sys

N = int(sys.stdin.readline())
T =[0]
P =[0]
for _ in range(N):
    a, b  = list(map(int, sys.stdin.readline().split()))
    T.append(a)
    P.append(b)
graph = []
cnt =0
def find(N):
    for i in range(1,N+1):
        cnt += T[i]
        graph.append(i)
        

print(T,P)
