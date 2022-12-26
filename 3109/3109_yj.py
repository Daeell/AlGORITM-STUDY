import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

R,C = map(int, input().split())
# print(R,C)
model = []
for i in range(R) :
    tmp = []
    for j in input().strip() :
        tmp.append(j)
    model.append(tmp)

# print(model)

def check(x,y):
    if x<0 or y<0 or x>=R or y>=C or model[x][y] == 'x' or model [x][y] == 'p' : 
        return False ; 
    else: 
        return True; 

def installIfPossible(x,y): 
    if check(x,y):
        model[x][y] = 'p'
        return True 
    else: 
        return False 

for i in range(R) :
    for j in range(C):
        if model[i][j] != 'x':
        # 오른쪽 위 확인
            print("체크" ,i,j)
            if installIfPossible(i-1,j+1) : 
                continue 
            # 오른쪽 확인
            if installIfPossible(i,j+1) :
                continue 
            # 오른쪽 아래 확인 
            if installIfPossible(i+1,j+1) :
                continue
    
for row in model : 
    print(row)

