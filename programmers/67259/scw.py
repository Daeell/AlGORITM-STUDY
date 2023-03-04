import sys
from collections import deque
def solution(board):
    N = len(board)
    max_size = sys.maxsize
    answer = max_size 

    def bfs(y,x,cost, answer):
        dq = deque()
        directiton = [(0,1),(1,0),(0,-1),(-1,0)]
        price = [[max_size]*N for _ in range(N)]
        price[0][0] = 0
        
        dq.append((y, x, -1, 0)) # y좌표, x좌표, 방향, cost // 초기 방향은 -1인 이유는 어딜 가도 100 이니깐
        
        while dq:
            i, j, di, cur_cost = dq.popleft()

            if i == N-1  and j == N-1 and answer> cur_cost:
                answer = cur_cost
                continue # 항상 먼저 도착했다고해서 최소는 아니니깐 계속 진행
            
            for k in range(4): # 방향은 수직과 수평이 아닌 가는 동서남북 으로 확인을 해야함
                ny = i + directiton[k][0]
                nx = j + directiton[k][1]
                
                if 0<=nx<N and 0<=ny<N and board[ny][nx]==0:
                    if di == -1:
                        cost = cur_cost+100
                    elif di == k:
                        cost = cur_cost+100
                    else:
                        cost = cur_cost+600
                    
                    if price[ny][nx] < cost -400: # 아래 예시를 통해서 확인 꺾여서 들어오는 순간엔 더 클수 있으나 그 다음 블럭에서는 더 작을 수 있음
                        continue # 아래 예시의 답은 4500 / 기존의 것은 4900이 출력됨
                    
                    price[ny][nx] = cost
                    dq.append((ny, nx, k, cost))

        return answer
        

    answer = bfs(0,0,0, answer)

    return answer

print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))