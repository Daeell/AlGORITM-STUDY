import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dx = (1, 1, -1, -1, 1, -1, 0, 0)
dy = (0, 1, 0, 1, -1, -1, 1, -1)


def dfs(h, w):
    mat[h][w] = 0

    for i in range(8):
        n_h = h + dy[i]
        n_w = w + dx[i]

        if 0 <= n_w < w and 0 <= n_h < h and mat[h][w] == 1:
            dfs(n_h, n_w)


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    mat = [list(map(int, input().split())) for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if mat[i][j] == 1:
                dfs(i, j)
                ans += 1
