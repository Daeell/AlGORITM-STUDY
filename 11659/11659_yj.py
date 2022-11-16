import sys
sys.stdin= open("input.txt", "r")
input= sys.stdin.readline

N, M  = map(int,input().split())
acc = [0]
acc.extend(input().split()) # 아직 개행문자 들어가 있음
for i in range(1,N+1) :
    acc[i] = acc[i-1]+ int(acc[i])

for k in range(M):
    i, j = map(int, input().split())
    print(acc[j]-acc[i-1])
    