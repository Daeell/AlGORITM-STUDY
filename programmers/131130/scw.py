#혼자놀기의달인

def solution(cards):
    answer = 0
    score =[]
    score_temp=0
    
    def check_score(num, idx, score, score_temp):
        
        while cards[idx]:
            num = cards[idx]-1
            cards[idx] = False
            score_temp +=1
            idx = num
        score.append(score_temp)
        score_temp = 0
    
    for i in range(len(cards)):
        if cards[i]:
            check_score(cards[i], i, score, score_temp)

    if len(score) >1:
        score.sort(reverse=True)
        answer = score[0]*score[1]
    else:
        answer =0
    return answer


print(solution([2, 3, 4, 5, 6, 7, 8, 9, 10, 1]))