# This is optimized code. Reduced time complexity by 20ms.
# 33088KB, 100ms

from collections import deque
import sys
import math

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
parked_cnt = 0

for _ in range(2*M):
    car = int(input())
    if car < 0:
        if wait_list:
            waiting_car = wait_list.popleft()
            car_area_map[waiting_car] = car_area_map[abs(car)]
            idx = int(math.log2(car_area_map[abs(car)]))
            total += area_table[idx] * car_table[waiting_car]
        else:
            parkingLot = parkingLot | car_area_map[abs(car)]
            parked_cnt -= 1
        continue

    if parked_cnt >= N:
        wait_list.append(car)
        continue

    for i in range(1, N+1):
        if parkingLot & 1 << i :
            car_area_map[car] = 1 << i
            parkingLot = parkingLot & ~(1 << i)
            total += area_table[i] * car_table[car]
            parked_cnt += 1
            break

print(total)