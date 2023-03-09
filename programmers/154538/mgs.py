from collections import deque

def bfs(x, y, n, res) :
    check_val = deque()
    check_val.append(x)
    while check_val :
        tmp = check_val.popleft()
        if tmp == y :
            return res[tmp]
        
        for val in [tmp+n, tmp*2, tmp*3] :
            if val > y :
                continue
            if not res[val] :
                res[val] = res[tmp] + 1
                check_val.append(val)
    return -1
def solution(x, y, n):
    res = [0 for _ in range((10**6)+1)]
    answer = bfs(x, y, n, res)
    return answer

print(solution(2, 5, 4))
