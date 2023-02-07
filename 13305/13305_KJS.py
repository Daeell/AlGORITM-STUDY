import sys
N = int(sys.stdin.readline())
distance =list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))
min_oil = 1000000001
cost = 0

for i in range(1,N):
    min_oil = min(min_oil, oil[i-1])
    cost += distance[i-1] * min_oil

print(cost)
