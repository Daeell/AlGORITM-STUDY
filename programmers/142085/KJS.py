def solution(n, k, enemy):
    answer = 0
    for i in range(len(enemy)):
        if n >= enemy[i] and n - enemy[i] >= 0:
            n -= enemy[i]
            answer +=1
        else:
            if k > 0:
                k -=1
                answer +=1
            else:
                break
    return answer
