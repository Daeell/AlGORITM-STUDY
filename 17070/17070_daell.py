import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
matt = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

garo = "g"
sero = "s"
daegak = "d"


def dfs(now_c, now_r, dir_):
    global cnt
    if now_c == n-1 and now_r == n-1:
        cnt += 1
        return
    if dir_ == garo or dir_ == daegak:
        if now_r+1 < n and matt[now_c][now_r+1] != 1:
            dfs(now_c, now_r+1, garo)
    if dir_ == sero or dir_ == daegak:
        if now_c+1 < n and matt[now_c+1][now_r] != 1:
            dfs(now_c+1, now_r, sero)
    if now_r+1 < n and now_c+1 < n:
        if matt[now_c+1][now_r+1] != 1 and matt[now_c][now_r+1] != 1 and matt[now_c+1][now_r] != 1:
            dfs(now_c+1, now_r+1, daegak)


dfs(0, 1, garo)

print(cnt)
