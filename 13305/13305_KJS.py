import sys
N = int(sys.stdin.readline())
distance = [0]
distance.extend(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))
oil = [0] + oil
for i in range(1,N):
    cost[i] += cost[i-1]+oil[i-1] * distance[i] 
    print(cost[i])

print(cost)
