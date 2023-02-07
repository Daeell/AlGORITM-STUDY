from collections import Counter

def solution(k, tangerine):
    answer = 0
    tangerine_counter = Counter(tangerine).most_common()
    cnt = 0
    for i in range(len(tangerine_counter)):
        if k > tangerine_counter[i][1]:
            k -= tangerine_counter[i][1]
            cnt +=1
        elif k == tangerine_counter[i][1]:
            cnt +=1
            return cnt
        else:
            cnt +=1
            return cnt
    
    
    answer = cnt
    
    
    return answer
