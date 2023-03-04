def solution(m, n, board):
    # 판 정보를 2차원 리스트 형태로 변환
    board = [list(row) for row in board]
    count = 0
    while True:
        removed = set()
        # board를 순회한다. (반복)
        for i in range(m-1):
            for j in range(n-1):
                # 순회하면서 4개의 리스트가 모두 겹치는 것이 있으면 제거 목록에 넣는다.
                if board[i][j] != '-' and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    removed.add((i, j))
                    removed.add((i+1, j))
                    removed.add((i, j+1))
                    removed.add((i+1, j+1))

        # 제거 목록에 아무 것도 없으면 break
        if not removed:
            break

        # 제거 목록에 있으면 그것들을 다 -로 바꿈
        for i, j in removed:
            board[i][j] = "-"

        for j in range(n):
            for i in range(m-1, 0, -1):
                if board[i][j] == "-":
                    # 블록을 계속 내려줌
                    k = i - 1
                    while k >= 0 and board[k][j] == "-":
                        k -= 1
                    if k < 0:
                        break
                    board[i][j] = board[k][j]
                    board[k][j] = "-"

    # 제거가 모두 끝난 이후니까 제거된 블록을 싹 세어줌.
    for i in range(m):
        for j in range(n):
            if board[i][j] == "-":
                count += 1

    return count


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
