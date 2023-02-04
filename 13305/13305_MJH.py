import sys
input = sys.stdin.readline
# 아이디어:
#   최종적으로는, 제일 저렴한 도시에서 남은 거리에 해당하는 기름을 다 넣는게 이득
#   출발지의 기름값보다 가격이 싼 도시가 있으면 그곳까지만 갈 수 있게 기름을 주유

CITY_NUM = int(input())

roadLengthArr = [0] + list(map(int, input().split()))
oilPriceArr = list(map(int, input().split()))

totalPrice = 0
cur = 0

for i in range(CITY_NUM):
    if oilPriceArr[cur] <= oilPriceArr[i]:
        continue

    totalPrice += oilPriceArr[cur] * sum(roadLengthArr[cur+1:i+1])
    cur = i

totalPrice += oilPriceArr[cur] * sum(roadLengthArr[cur+1:i+1])

print(totalPrice)