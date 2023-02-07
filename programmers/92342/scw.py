# def solution(n, info):
#     answer = []
    
#     def find_max(n):
#         temp=10
#         s=0
#         maxi=0
#         while(s<n):
#             maxi +=temp
#             s +=1
#             temp -=1
#         return maxi
    
#     maxi=find_max(n)

#     apeach_score =0
#     for i in range(len(info)):
#         if info[i] !=0:
#             apeach_score +=(10-i)
    
#     if maxi == apeach_score:
#         answer.append(-1)
#         return answer
    


#     print(maxi)
            

#     return answer


# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))

from itertools import product # permutation, combination 등처럼 순열을 만들어주는 모듈

def solution(n, info):
    answer=[-1]
    info.reverse() # info 순서는 0점부터 ~ 10 점 순으로 변경
    max_score=0
    for score_board in product((True, False), repeat=11): # 11칸의 리스트를 True False 로 채운 모든 경우의 수를 줌

        shoot_count = sum(info[i]+1 for i in range(11) if score_board[i]) # Ryan이 이길 수 있는 화살 개수
        
        if shoot_count<=n: # Ryan이 이길 수 있는 화살 개수가 쏠수 있는 화살개수 이하 일 경우
            apeach_score = sum(i for i in range(11) if not score_board[i] and info[i]) # 이때 appeach의 점수를 보고
            ryan_score = sum(i for i in range(11) if score_board[i]) # ryan의 점수를 보고
            diff_score = ryan_score - apeach_score # 둘의 차를 계산하고

            if diff_score > max_score: # 그 차이가 최대인지 확인하고
                max_score = diff_score
                answer = [info[i]+1 if score_board[i] else 0 for i in range(11)] # 그때의 answer list를 저장
                answer[0] += n-shoot_count # 남은 화살 개수를 0번칸에 넣어줌 (가장 낮은 점수를 더 많이 맞춘 경우)
            
    answer.reverse() # 10에서 0점 순으로 뒤집어주고
    return answer



print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))