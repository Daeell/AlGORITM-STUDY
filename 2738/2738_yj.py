import sys
sys.stdin= open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
A= list()
B= list()
for i in range(N) :
    A.append(list(map(int, input().split())))

for i in range(N) :
    B.append(list(map(int, input().split())))


result = list([  0 for _ in range(M)  ] for _ in range(N))
for i in range(N):
    for j in range(M):
        result[i][j]= A[i][j] + B[i][j]

for i in range(N):
    print(*result[i])
