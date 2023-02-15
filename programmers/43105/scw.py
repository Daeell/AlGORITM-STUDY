def solution(triangle):
    dp = [0]*(len(triangle)+1)
    print(triangle)
    print(dp)
    dp[0] = triangle[0][0]
    dp[1] = max(triangle[1]) + dp[0]

    if len(triangle) >=2:
        for i in range(2, len(triangle)):
            for j in range(len(triangle[i])):
                if j ==0:
                    dp[i]=max(triangle[i][j] + triangle[i-1][j] +dp[i-2], dp[i])
                elif j ==len(triangle[i])-1:
                    dp[i]=max(triangle[i][j] + triangle[i-1][j-1]+dp[i-2], dp[i]) 
                else:
                    dp[i]=max(triangle[i][j] + triangle[i-1][j]+dp[i-2],triangle[i][j] + triangle[i-1][j-1] +dp[i-2], dp[i])
    answer = 0
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))