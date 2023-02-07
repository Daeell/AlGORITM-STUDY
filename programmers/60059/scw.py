def key_rotation(key):
    new_key = [[0 for _ in range(len(key))] for _ in range(len(key))]
    n = len(new_key)

    for x in range(n):
        for y in range(n):
            new_key[x][y] = key[y][abs(x-(len(key)-1))]
    return new_key

def check(key, M, N, new_lock, i, j):

    checking_lock = [[0 for  _ in range(N*3)] for _ in range(N*3)] # checking용 lock임 여기가 가득차면 True가 될거
    
    for x in range(N, N+N): # checking 용 lock을 하나 더 만들어줌
        for y in range(N, N+N):
            checking_lock[x][y] = new_lock[x][y]
    
    for x in range(i, i+M): # key를 checking용 lock에다가 넣어줌
        for y in range(j, j+M):
            checking_lock[x][y] += key[x-i][y-j]
    
    for x in range(N, N+N): # checking_lock 중 하나라도 False 이면 False
        for y in range(N, N+N):
            if checking_lock[x][y] != 1: # 자물쇠 영역과 키가 중복되면 안됨 (lock 중간 안에서는)
                return False
    return True

def solution(key, lock):
    answer = False
    M, N = len(key), len(lock)
    
    # 새로운 lock을 만듦 -- 기존 lock의 3배크기 = 이유: 키를 돌리면서 넣어야하는데 꼭지점에 한칸만 걸치는 경우를 감안
    new_lock = [[0 for _ in range(N*3)] for _ in range(N*3)]
    
    # 새로운 lock의 중간에 기존 lock을 넣어줌
    for i in range(N, N+N):
        for j in range(N, N+N):
            new_lock[i][j] = lock[i-N][j-N]

    for _ in range(4):
        key = key_rotation(key) # key를 90도로 돌려줌

        for i in range(N-M+1, N+N): # key 가 lock - key +1 해서 시작점
            for j in range(N-M+1, N+N):
                answer = check(key, M, N, new_lock, i, j) # lock이 풀리나 확인
                if answer == True:
                    return answer

    return answer



print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))