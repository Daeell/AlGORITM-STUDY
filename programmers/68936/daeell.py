def solution(arr):
    n = len(arr)
    answer = [0, 0]
    quad(arr, [0, 0], n, answer)
    return answer


def quad(arr, start, length, answer):
    row, col, target = start[0], start[1], arr[start[0]][start[1]]
    for i in range(length):
        for j in range(length):
            if arr[row + i][col + j] != target:
                half = length // 2
                quad(arr, start, half, answer)
                quad(arr, [row, col + half], half, answer)
                quad(arr, [row + half, col], half, answer)
                quad(arr, [row + half, col + half], half, answer)
                return
    answer[target] += 1


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [
      0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
