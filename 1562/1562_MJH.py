def main(N):
    if N < 10:
        return 0

    BILLION = 1000000000
    VALID_NUM = (1<<10)-1
    dp = [[0 for _ in range(1<<10)] for _ in range(10)]
    for i in range(1, 10):
        dp[i][1<<i] = 1

    for _ in range(1, N):
        dp_next = [[0 for _ in range(1<<10)] for _ in range(10)]
        for i in range(10):
            for j in range(1 << 10):
                if i > 0:
                    dp_next[i][(1<<i)|j] = (dp_next[i][(1<<i)|j] + dp[i-1][j]) % BILLION
                if i < 9:
                    dp_next[i][(1<<i)|j] = (dp_next[i][(1<<i)|j] + dp[i+1][j]) % BILLION
        dp = dp_next

    return sum(dp[i][VALID_NUM] for i in range(10)) % BILLION


print(main(int(input())))