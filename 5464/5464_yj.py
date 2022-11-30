import sys
from collections import deque  
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
price = [0] # 주차공간의 단위 무게당 요금 (0번 인덱스 사용 X)
weight = [0] # 차량무게  (0번 인덱스 사용 X)
parkinglot= [0 for _ in range(N+1)] # 주차장  (0번 인덱스 사용 X)
whereisthecar= [0 for _ in range(N+1)] # 주차현황  (0번 인덱스 사용 X)
profit = 0 
for i in range(N): 
    price.append(int(input()))
for i in range(M):
    weight.append(int(input()))

q = deque()
for i in range(2*M): 
    q.append(int(input()))

# print(q)
# print(price)
# print(weight)
# print(parkinglot)

for i in range(2*M):
    car = q.popleft()
    if (car >0 ): # 주차 
        # first-fit 방식으로 탐색 - 빈 공간 만나면 바로 주차시킴 
        for i in range(1, N+1) :# 주차 공간을 1번 인덱스부터 N번 인덱스 까지 순회 탐색
            if (parkinglot[i] == 0 ) :
                parkinglot[i] = car
                whereisthecar[car] = i
                profit += price[i]*weight[car]
                # print(profit)
                break
    else : # 출차 
        parkinglot[whereisthecar[car]] = 0 

print(profit)