#귤 고르기

from collections import defaultdict

def solution(k, tangerine):
    A = defaultdict(int)
    answer =0
    for i in tangerine:
        A[i] +=1
    A_sort= sorted(A.items(), key = lambda item: item[1], reverse = True)
    
    sum_AA=0
    for key, i in A_sort :
        if sum_AA < k:
            sum_AA+=i
            answer +=1
        else :
            break
            
    return answer