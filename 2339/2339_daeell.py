import sys
sys.stdin = open('python/input.txt', 'r')
input = sys.stdin.readline


def cut(sr, sc, er, ec, garo):
    bosuk = 0
    boolsoon = 0
    for r in range(er):
        for c in range(ec):
            if board[er][ec] == '1':
                bosuk += 1
            elif board[er][ec] == '2':
                boolsoon += 1


def check(row, col):
    bosuk = 0
    boolsoon = 0
    for row in range(N):
        for col in range(N):
            if board[row][col] == '1':
                boolsoon += 1
            elif board[row][col] == '2':
                bosuk += 1
    return (bosuk, boolsoon)


N = int(input())
board = [input().rsplit() for _ in range(N)]
cnt = 0
(bosuk, boolsoon) = check(N, N)
if bosuk == 1 and boolsoon == 0:
    cnt = 1
else:
    cutSero = cut(0, 0, N, N, "sero")
    cutGaro = cut(0, 0, N, N, "garo")
