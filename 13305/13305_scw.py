#주유소
import sys
input=sys.stdin.readline

N=int(input().strip())
road = list(map(int,input().strip().split()))
money = list(map(int,input().strip().split()))


# 41점
# answer=0
# for i in range(1,N+1):
#     tempmin = 1000000001
#     for j in range(i):
#         if i-1 == len(road):
#             break
#         tempmin=min(money[j]*road[i-1],tempmin)
#     answer+=tempmin

# print(answer-tempmin)

# 100점
answer=0
min_money=1000000001
for i in range(1,N):
    min_money=min(min_money, money[i-1])
    answer += min_money*road[i-1]

print(answer)