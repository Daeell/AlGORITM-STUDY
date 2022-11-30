import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
parking = [0]
cars = [0]
for _ in range(N):
    parking.append(int(sys.stdin.readline()))
for _ in range(M):
    cars.append(int(sys.stdin.readline()))
cost = 0
queue = []

for i in range(2*M):
    nums = int(sys.stdin.readline())
    if nums > 0:
        if len(queue) < N-1:
            queue.append(nums)
            cost += (cars[nums]) * parking[(queue.index(nums)+1)]
    else:
        
        
            


print(parking, cars)
