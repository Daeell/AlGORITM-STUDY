import sys
def main():
    arr = [0]*5
    for i in range(5):
        arr[i] = list(sys.stdin.readline().split())

    x_offset = [-1, 0, 0, 1]
    y_offset = [0, -1, 1, 0]

    answers = set()

    def DFS(x: int, y: int, count: int, number: str) -> None:
        if count == 6:
            answers.add(number)
            return
        for k in range(4):
            if x + x_offset[k] < 0 or y + y_offset[k] < 0 or x + x_offset[k] > 4 or y + y_offset[k] > 4:
                continue
            DFS(x + x_offset[k], y + y_offset[k], count + 1, number + arr[x][y])

    for i in range(5):
        for j in range(5):
            DFS(i, j, 0, '')

    print(len(answers))


main()