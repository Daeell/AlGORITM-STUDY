import sys
input = sys.stdin.readline

def horizontal(pipe_r, pipe_c) -> int:
    global arr, dp_h, N

    # Enter only if not visited.
    if dp_h[pipe_r][pipe_c] == -1:
        cnt = 0

        if arr[pipe_r][pipe_c+1] == 0:
            cnt += horizontal(pipe_r, pipe_c+1)
            
            if arr[pipe_r+1][pipe_c+1] == 0 and arr[pipe_r+1][pipe_c] == 0:
                cnt += diagonal(pipe_r+1, pipe_c+1)
    
        dp_h[pipe_r][pipe_c] = cnt

    return dp_h[pipe_r][pipe_c]

def vertical(pipe_r, pipe_c) -> int:
    global arr, dp_v, N

    # Enter only if not visited.
    if dp_v[pipe_r][pipe_c] == -1:
        cnt = 0

        if arr[pipe_r+1][pipe_c] == 0:
            cnt += vertical(pipe_r+1, pipe_c)
            
            if arr[pipe_r+1][pipe_c+1] == 0 and arr[pipe_r][pipe_c+1] == 0:
                cnt += diagonal(pipe_r+1, pipe_c+1)
    
        dp_v[pipe_r][pipe_c] = cnt

    return dp_v[pipe_r][pipe_c]

def diagonal(pipe_r, pipe_c) -> int:
    global arr, dp_d, N

    # Enter only if not visited.
    if dp_d[pipe_r][pipe_c] == -1:
        cnt = 0

        if arr[pipe_r][pipe_c+1] == 0:
            cnt += horizontal(pipe_r, pipe_c+1)

        if arr[pipe_r+1][pipe_c] == 0:
            cnt += vertical(pipe_r+1, pipe_c)
            
            if arr[pipe_r+1][pipe_c+1] == 0 and arr[pipe_r][pipe_c+1] == 0:
                cnt += diagonal(pipe_r+1, pipe_c+1)
    
        dp_d[pipe_r][pipe_c] = cnt

    return dp_d[pipe_r][pipe_c]

def main():
    global arr, dp_h, dp_v, dp_d, N
    N = int(input().strip())
    arr = []

    # Input to array (room info).
    for _ in range(N):
        arr.append(list(map(int, input().split()))+[1])
    arr.append([1]*(N+1))   # Make safety wall.

    # Make DP for each case, and set the end point value.
    dp_h = [[-1]*N for _ in range(N)]
    dp_h[N-1][N-1] = 1

    dp_v = [[-1]*N for _ in range(N)]
    dp_v[N-1][N-1] = 1

    dp_d = [[-1]*N for _ in range(N)]
    dp_d[N-1][N-1] = 1

    # Set the initial pipe.
    pipe_r = 0
    pipe_c = 1

    print(horizontal(pipe_r, pipe_c))

main()