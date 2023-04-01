import sys
input = sys.stdin.readline
def main():
    H, W = map(int, input().split())
    board = [[0 for _ in range(W)] for _ in range(H)]
    blocks = list(map(int, input().split()))
    for i in range(len(blocks)):
        for j in range(blocks[i]):
            board[H-1-j][i] = 1

    cnt = 0
    for i in range(len(board)):
        block_idx = -1
        for j in range(len(board[0])):
            if (board[i][j] == 1):
                if block_idx > -1:
                    cnt += j - block_idx - 1
                block_idx = j

    return cnt

print(main())