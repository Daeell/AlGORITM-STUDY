def solution(key, lock):
    answer = True

    re_lock = []
    re_key = []

    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if lock[i][j] == 0:
                re_lock.append((i,j))

    for i in range(len(key)):
        for j in range(len(key[0])):
            if key[i][j] == 1:
                re_key.append((i,j))
    print(re_lock)
    print(re_key)
    # while
    # key rotation
    # key move
    # 둘이 일치하면 true로 탈출
    # 둘이 일치하지 않으면 false

    return answer



print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))