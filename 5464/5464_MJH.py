from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

area_table = [0]*(N+1)
car_table = [0]*(M+1)

for i in range(1, N+1):
    area_table[i] = int(input())

for i in range(1, M+1):
    car_table[i] = int(input())

car_area_map = [0]*(M+1)
total = 0
parkingLot = (2**(N+1)) - 1
wait_list = deque()

for _ in range(2*M):
    car = int(input())
    if car < 0:
        parkingLot = parkingLot | car_area_map[abs(car)]
        if wait_list:
            car = wait_list.popleft()
        else:
            continue

    for i in range(1, N+1):
        if parkingLot | 1 << i :
            car_area_map[car] = 1 << i
            parkingLot = parkingLot | ~(1 << i)
            total += area_table[i] * car_table[car]
    if car_area_map[car] == 0:
        wait_list.append(car)

print(total)