import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

mat = [list(map(str, input().split())) for _ in range(5)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
numbers = set()


def dfs(row, col, number):
    if len(number) == 6:
        numbers.add(number)
        return

    for i in range(4):
        n_row = row + dx[i]
        n_col = col + dy[i]

        if 0 <= n_row < 5 and 0 <= n_col < 5:
            dfs(n_row, n_col, number + mat[n_row][n_col])


for row in range(5):
    for col in range(5):
        dfs(row, col, mat[row][col])

print(len(numbers))
