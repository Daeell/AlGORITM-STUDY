# 4 8 2
# 1 2 4
# 1 3 2
# 1 4 7
# 2 1 1
# 2 3 5
# 3 1 2
# 3 4 4
# 4 2 3

import sys
sys.stdin = open("input.txt", "r")
input= sys.stdin.readline

N, M, X = map(int, input().split())
maxval = sys.maxsize
arr = list([ maxval for _ in range(N+1) ] for _ in range(N+1))

for i in range(M) :
    a, b, t = map(int, input().split())
    arr[a][b] = t
print(arr)

def getshortest(i, visited) :
    minval = maxval
    minnode = maxval
    
    for k in range(1, N+1):
        if k in visited: 
            continue
        if arr[i][k] < minval :
            minval = arr[i][k]
            minnode = k 

    return minnode 


def getmincost(i, arr) : 
    visited = set()
    visited.add(i) 

    while (len(visited) == N) :     
        shortest = getshortest(i, visited) #shortest 최단 거리의 노드 

        #shortest를 통해서 가는 최단 경로를 다시 계산 
        visited.add(shortest)

        for k in range(1, N+1) :
            if k ==1 :
                continue 
            arr[i][k] = min(arr[i][k], arr[i][shortest]+ arr[shortest][i])
        
    


    # for k in range(1, N+1) :
    #     if k not in visited : # 방문하지 않은 노드라면 


for i in range(1, N+1) :
    if i == X :
        continue 

    getmincost(i, arr)

print("after")

print(arr)


minval = maxval
for i in range(1, N+1):
    if arr[i][X] + arr[X][i] < minval :
        minval = arr[i][k]
        minnode = k 

    # minval = min(minval, arr[i][X] + arr[X][i]) 
