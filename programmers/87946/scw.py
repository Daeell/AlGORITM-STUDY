#피로도

def solution(k, dungeons):
    answer = -1
    a = len(dungeons)
    temp = [[0,0]]
    dungeons = temp + dungeons
    
    dp=[[k]*(a+1) for _ in range(a+1)]

    for i in range(1,a+1):
        for j in range(1,a+1):
            min_piro, somo_piro = dungeons[i][0], dungeons[i][1]
            pilyeo, somo = dungeons[j][0], dungeons[j][1]
            # print(weight, val)
            if pilyeo<=min_piro:
                dp[i][j]=min(dp[i-1][j],dp[i-1][j] - somo)
            else:
                dp[i][j]=dp[i-1][j]
        
        
    
    print(dp)
    return answer