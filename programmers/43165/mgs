from collections import deque

def bfs(numbers, target) :
    tmp = deque()
    res = 0
    tmp.append([numbers[0], 0])
    tmp.append([numbers[0] *(-1), 0])
    while tmp :
        x, cnt = tmp.popleft()
        
        if cnt == len(numbers)-1:
            if x == target:
                res += 1
            continue
        dx = [1, -1]
        for i in range(2) :
            nx = numbers[cnt+1] * dx[i]
            tmp.append([x+nx, cnt+1])

        
    return res

def solution(numbers, target):
    answer = bfs(numbers, target)
    return answer
