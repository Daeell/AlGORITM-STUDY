import sys
sys.stdin= open("input.txt", "r")
input= sys.stdin.readline

N = int(input())
arr = [0]
for i in range(N):
    arr.append(tuple(map(int,input().split())))
print(arr)

tmp = [] # 모든 보수의 합을 담아 놓은 배열 
profit = 0 

start = arr[i] 
def do (i, profit):
    # 일을 했을 때
    if (i>N) : 
        return ; 
    if ((i + arr[i][1]) <= N) :  
        donot(i, profit) # 일을 안한 경우 
        
        i += arr[i][0]
        profit += arr[i][1] 
        do(i, profit)
    
    dont(i, profit)

def donot (i, profit) :
    # 일을 안했을 때 
    i += 1
    do(i, profit)
    


do(1, profit)
dont(1, profit)
