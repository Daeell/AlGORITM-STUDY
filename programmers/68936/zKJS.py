def dfs(x,y,n,arr,answer):
    check = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != arr[i][j]:
                check = -1
                break
    if check == -1:
        n = n //2
        dfs(x,y,n,arr,answer)
        dfs(x,y+n,n,arr,answer)
        dfs(x+n,y,n,arr,answer)
        dfs(x+n,y+n,n,arr,answer)
    elif check == 1:
        answer.append(1)
    else:
        answer.append(0)
        

def solution(arr):
    n = len(arr)
    answer = []
    dfs(0,0,n,arr,answer)
    res = [answer.count(0),answer.count(1)]
    return res
