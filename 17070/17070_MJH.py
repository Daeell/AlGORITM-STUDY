import sys
from enum import Enum
input = sys.stdin.readline

def horizontal(pipe_r, pipe_c, cnt) -> int:
    global arr
    if arr[pipe_r][pipe_c+1] == 1:
        return cnt

    if arr[pipe_r+1][pipe_c+1] == 0 and arr[pipe_r+1][pipe_c] == 0:
        cnt += diagonal(pipe_r+1, pipe_c+1, cnt)
    
    cnt += horizontal(pipe_r, pipe_c+1, cnt)

    return cnt

def vertical(pipe_r, pipe_c, cnt) -> int:
    global arr

def diagonal(pipe_r, pipe_c, cnt) -> int:
    global arr
    if arr[pipe_r][pipe_c+1] == 0:
        cnt += horizontal(pipe_r, pipe_c+1, cnt)

    if arr[pipe_r+1][pipe_c] == 0:
        cnt += vertical(pipe_r+1, pipe_c, cnt)

        if arr[pipe_r+1][pipe_c+1] == 0 and arr[pipe_r][pipe_c+1] == 0:
            cnt += diagonal(pipe_r+1, pipe_c+1, cnt)
    
    cnt += horizontal(pipe_r, pipe_c+1, cnt)

    return cnt

def main():
    global arr
    N = int(input().strip())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    pipe_r = 0
    pipe_c = 1
    horizontal(pipe_r, pipe_c, 0)