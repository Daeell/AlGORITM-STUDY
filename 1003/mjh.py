import sys

def main():

    def fibonacci(num):
        if num == 0:
            return dp[0]
        elif num == 1:
            return dp[1]
        else:
            if dp[num][0] != 0 or dp[num][1] != 0:
                return dp[num]
            else:
                dp[num][0] = fibonacci(num-1)[0] + fibonacci(num-2)[0]
                dp[num][1] = fibonacci(num-1)[1] + fibonacci(num-2)[1]
                return dp[num]
            

    T = int(sys.stdin.readline())
    for _ in range(T):
        dp = [[0, 0] for _ in range(41)]
        dp[0][0] = 1
        dp[1][1] = 1

        n = int(sys.stdin.readline())
        answer = fibonacci(n)
        print(answer[0], answer[1])
            
main()