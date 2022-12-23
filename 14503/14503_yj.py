import sys
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline

N,M = map(int, input().split())
global r
global c
global d

r, c, d = map(int, input().split())


room = []
for i in range(N):
    room.append(list(map(int, input().split())))
# d : 0북, 1동, 2남, 3서쪽
dx = [0,1,0,-1]
dy = [-1,0,1,0]

def clean_it_up() : 
    room[r][c] = 2 

def turn_left():
    #0->3->2->1
    global d
    if d == 0 : 
        d= 3
    else: 
        d -=1 

def check_left(): # 청소 안된 공간이면 true 
    global r
    global c
    global d
    turn_left() #우선 왼쪽 방향으로 돈 후 
    if room[r+dy[d]][c+dx[d]] == 0 : #청소되지 않은 공간이라면 
        return True 
    else: 
        return False 

def is_wall_behind(): # 뒤가 벽인가? 
    global r
    global c
    global d
    if room[r+dy[(d+2)%4]][c+dx[(d+2)%4]] == 1 : #뒤가 벽이라면 
        return true 
    else: 
        return false 

def step_ahead(): #앞으로 한칸 
    global r
    global c
    global d
    r= r+dy[d]
    c= c+dx[d]

def step_back(): #뒤로 한칸 
    global r
    global c
    global d
    r= r+dy[(d+2)%4]
    c= c+dx[(d+2)%4]

def check_around(): 
    global r
    global c
    global df
    for i in range(4) :
        if (check_left()) : #왼쪽에 청소할 공간이 있으면
            turn_left() #돌아서 
            step_ahead() #앞으로 가 
            return True 
        else: 
            i +=1 
            turn_left()
    return False

# 1. 현재 위치를 청소한다.
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
#    2-1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
#    2-2. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
#    2-3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
#    2-4. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

flag = True 

while (flag) : 
    clean_it_up()
    if check_around() :
        print("무한루프")
        continue 
    else :
        
        if (not is_wall_behind()):
            step_back()
            continue 
        else: 
            flag = False 

cnt = 0 

for i in range(N):
    for j in range(M):
        if room[i][j]==2 :
            cnt +=1 

print(cnt)
