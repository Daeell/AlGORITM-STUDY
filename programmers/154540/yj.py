def check(param) :
    if param == 'X' : 
        return 0 
    else: 
        return int(param)

def dfs(visited, array, h,w, tmp, height, width) :
    visited[h][w]= True # 방문 처리
    print("11현재 visited 상태", visited)
    tmp += check(array[h][w]) #값 더하기 

    # 이어진 모든 곳들도 방문하면서 tmp 더하기 
    for d in [(0,-1), (0,1), (1,0), (-1,0)] : 
        if 0 <= h+d[1] < height and  0 <= w+d[0] < width :
            if visited[h+d[1]][w+d[0]] == False :
                tmp = dfs(visited, array, h+d[1], w+d[0], tmp, height, width)
                print("현재 visited 상태", visited)
    return tmp

def solution(maps):
    width = len(maps[0])
    height = len(maps)
    array = []
    for m in maps :
        tmp = []
        for i in range(width) :
            tmp.append(m[i])
        array.append(tmp)
    # print(array) #! 2차원 배열 완성 

    # dfs로 순회
    visited = [ [False]* width ]* height
    answer = []

    for h in range(height):
        for w in range(width) :
            if visited[h][w] == False : 
                print("go DFS !! ")
                tmp = dfs(visited,array, h,w, 0, height, width)
                if tmp >0 :
                    answer.append(tmp)

    print(answer)


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
