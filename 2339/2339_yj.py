import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N= int(input())
slate = []
for i in range(N):
    slate.append(list(map(int,input().split())))
# print(slate)

def divideIntoTwo(direction, x1,x2,y1,y2) :
    #! 가로로 잘랐었다면 이번엔 세로로, 세로로 잘랐었다면 이번엔 가로로! 
    if direction  :  
        direction = 1 #!세로로 자르기

        for i in range(y1+1, y2) : 
            dirty = 0 
            for j in range(x1, x2+1):
                slate[j][i]
    else :
        direction = 0 #! 가로로 자르기
    
    for i in range(N):
        slate[i]


#* 가로 시작 케이스 1개 (가로 0, 세로 1)
divideIntoTwo(0, 0, N-1, 0, N-1)

#* 세로 시작 케이스 1개  (가로 0, 세로 1)
divideIntoTwo(1, 0, N-1, 0, N-1)