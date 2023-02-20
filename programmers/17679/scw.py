from collections import deque

def solution(m, n, board):
    find_block_direction = [(0,1),(1,0),(1,1)]
    answer = 0
    temp = set()
    same_block=set()

    for i in range(m):
         board[i] = list(board[i])

    
    while True:
        for i in range(m-1):
            for j in range(n-1):
                block= board[i][j]
                if block == '':
                    continue
                temp.add((i,j))
                cnt = 1
                for dy, dx in find_block_direction:
                    ny = i + dy
                    nx = j + dx
                    if 0<=ny<m and 0<=nx<n and block != board[ny][nx]:
                        temp = set()
                        break
                    elif 0<=ny<m and 0<=nx<n and block == board[ny][nx]:
                        cnt +=1
                        if cnt ==4:
                            same_block.update(temp)
                            same_block.add((ny,nx))
                            break
                        temp.add((ny, nx))
        if len(same_block) == 0:
            break
        
        answer += len(same_block)
        while same_block:
                y, x = same_block.pop()
                board[y][x] = ""
        
        temp_list=deque()
        for i in range(n):
            for j in range(m):
                if board[j][i] != '':
                    temp_list.append(board[j][i])
                else : 
                    temp_list.appendleft('')
            
            for j in range(m):
                board[j][i] = temp_list.popleft()



    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))