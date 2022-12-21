import sys
from collections import deque  
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
price = [0] # 주차공간의 단위 무게당 요금 (0번 인덱스 사용 X)
weight = [0] # 차량무게  (0번 인덱스 사용 X)
parkinglot= [0 for _ in range(N+1)] # 주차장  (0번 인덱스 사용 X)
whereisthecar= [0 for _ in range(M+1)] # 주차현황  (0번 인덱스 사용 X)
profit = 0 
for i in range(N): 
    price.append(int(input()))
for i in range(M):
    weight.append(int(input()))

q = deque()
waitlist = deque() 
print("대기 리스트 길이 : ", len(waitlist))
for i in range(2*M): 
    q.append(int(input()))
flag = 0 
# print(q)
# print(price)
# print(weight)
# print(parkinglot)

for i in range(2*M):
    car = q.popleft()
    print("car는 ", car)
    if (car >0 ): # 주차 
        # first-fit 방식으로 탐색 - 빈 공간 만나면 바로 주차시킴 
        for i in range(1, N+1) : # 주차 공간을 1번 인덱스부터 N번 인덱스 까지 순회 탐색
            if (parkinglot[i] == 0 ) :
                parkinglot[i] = car
                print("주차공간", i,"에 주차한 차는", parkinglot[i])
                whereisthecar[car] = i-1
                profit += price[i]*weight[car]
                print(profit)
                flag = 1
                break
        # 여기까지 온다면 빈 공간이 없었던 것 
        if (flag) :
            print("여기 온 차? ", car)
            waitlist.append(car)

    else : # 출차 
        k = whereisthecar[car]
        print("대기 리스트 길이 : ", len(waitlist))
        print(car, "가 주차되어있던 곳은", k)
        if (len(waitlist) > 0): # 출차를 하려하는데 대기 리스트에 차가 있다면 
            j = waitlist.popleft()
            parkinglot[k] = j # 대기 리스트의 맨 앞 차를 그 자리에 넣어준다 
            whereisthecar[j] = k 
        else :
            parkinglot[k] = 0 
            print("이제 주차공간 ", k ,"는 ", parkinglot[k] )

            
print(profit)