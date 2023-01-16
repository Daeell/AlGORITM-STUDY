#피로도

# def solution(k, dungeons): -- 2차원 dp 실패
#     answer = -1
#     a = len(dungeons)
#     temp = [[0,0]]
#     dungeons = temp + dungeons
    
#     dp=[[k]*(a+1) for _ in range(a+1)]

#     for i in range(1,a+1):
#         for j in range(1,a+1):
#             min_piro, somo_piro = dungeons[i][0], dungeons[i][1]
#             pilyeo, somo = dungeons[j][0], dungeons[j][1]
#             # print(weight, val)
#             if pilyeo<=min_piro:
#                 dp[i][j]=min(dp[i-1][j],dp[i-1][j] - somo)
#             else:
#                 dp[i][j]=dp[i-1][j]
        
    
#     print(dp)
#     return answer

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for a in permutations(dungeons, len(dungeons)):
        total_piro=k
        cnt = 0
        for piro, somo in a:
            if piro<= total_piro and total_piro-piro >= 0:
                total_piro -=somo
                cnt+=1
        answer = max(cnt, answer)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
