def solution(triangle):
    dp = [[0]*i for i in range(1,len(triangle)+1)]
    dp[0][0] = triangle[0][0]

    if len(triangle) >=1:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j ==0:
                    dp[i][j]=max(triangle[i][j] + dp[i-1][j], dp[i][j])
                elif j ==i:
                    dp[i][j]=max(triangle[i][j] + dp[i-1][j-1], dp[i][j])
                else:
                    dp[i][j]=max(triangle[i][j] + dp[i-1][j],triangle[i][j] + dp[i-1][j-1], dp[i][j])
    answer = max(dp[-1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))