def solution(key, lock):
    n = len(lock)
    m = len(key)
    expanded_key = [[0] * (n + m - 1) for _ in range(n + m - 1)]

    for i in range(m):
        for j in range(m):
            expanded_key[i + (n - m) // 2][j + (n - m) // 2] = key[i][j]

    def is_valid_position(x, y):
        for i in range(n):
            for j in range(n):
                if lock[i][j] + expanded_key[i + x][j + y] == 2:
                    return False
        return True

    for _ in range(4):
        key = [list(row)[::-1] for row in zip(*key)]
        for x in range(-(n - 1), m):
            for y in range(-(n - 1), m):
                if is_valid_position(x, y):
                    return True

    # If no valid position is found, return False
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
