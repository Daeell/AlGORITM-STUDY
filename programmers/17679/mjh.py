# PASSED
def solution(m, n, board):
    answer = 0
    
    arr = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            arr[j][len(board)-1-i] = board[i][j]
        
    dx = (0, 1, 1, 0)
    dy = (1, 1, 0, 0)
    
    while True:
        del_list = []
        
        for i in range(len(arr)-1):
            for j in range(len(arr[0])-1):
                if arr[i][j] != '-':
                    flag = True
                    for k in range(3):
                        if arr[i+dx[k]][j+dy[k]] != arr[i][j]:
                            flag = False
                            break
                    if flag == True:
                        del_list.append((i, j))
                        
        if del_list == []:
            break
            
        for x, y in del_list:
            for i in range(4):
                arr[x+dx[i]][y+dy[i]] = 'del'

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                while arr[i][j] == 'del':
                    answer += 1
                    del arr[i][j]
                    arr[i].append('-')
    
    return answer