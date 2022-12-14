import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N,M,L,K = map(int, input().split())
meteorite = list()

width_min = sys.maxsize
width_max = 0
height_min = sys.maxsize
height_max = 0

for i in range(K) :
    tup = tuple(map(int, input().split()))
    width_min = min(tup[0], width_min)
    width_max = max(tup[0], width_max)
    height_min = min(tup[1], height_min)
    height_max = max(tup[1], height_max)
    meteorite.append(tup)

meteorite.sort(key = lambda x :(x[0], x[1]))
# print(meteorite)

# print(width_min)
# print(width_max)
# print(height_min)
# print(height_max)

# 트램펄린 범위는 가로: width_min ~ (width_max - L)
# 트램펄린 범위는 세로: height_min ~ (height_max - L)

hit_the_land = 0

#반복문 i, j는 트램펄린이 설치되는 왼쪽 아래 꼭지점의 좌표 
for i in range(width_min, width_max- L+1) : 
    for j in range(height_min, height_max- L+1) : 
        # 트램펄린은 가로 i~ i+L , 세로 j~ j+L 사이에 존재 
        tmp = 0
        for (x,y) in meteorite :
            # print("i,j, x,y " ,i,j,x,y)
            if ((x <i or x> i+L) and (y <j or y > j+L)) :
                tmp +=1 
        # print(tmp)
        hit_the_land = max(tmp, hit_the_land)

print(hit_the_land)



