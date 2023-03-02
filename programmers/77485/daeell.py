def solution(rows, columns, queries):
    answer = []
    matrix = [[(i-1)*columns+j for j in range(1, columns+1)]
              for i in range(1, rows+1)]
    print(matrix)

    for query in queries:
        print(query)
        r1, c1, r2, c2 = query
        tmp = matrix[r1-1][c1-1]
        min_num = tmp
        print(tmp)
        # 왼쪽 변
        for i in range(r1, r2):
            num = matrix[i][c1-1]
            matrix[i-1][c1-1] = num
            min_num = min(min_num, num)

        # 아래쪽 변
        for i in range(c1, c2):
            num = matrix[r2-1][i]
            matrix[r2-1][i-1] = num
            min_num = min(min_num, num)

    # 구현하다 끝남
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
