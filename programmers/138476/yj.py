# programmers/138476/

from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    dictionary = defaultdict(int)
    for i in tangerine :
        dictionary[i] += 1
        if dictionary[i] >= k : # 단일 갯수가 k보다 큰 사이즈가 있으면 바로 1 
            print(dictionary[i])
            answer = 1
            break

    # print(dictionary)
    inBox = 0 
    j = 1
    for i in sorted(dictionary.items(), key=lambda x: -x[1]) :
        inBox += i[1]
        # print("=========",inBox)
        if inBox >= k :
            # print("true")
            answer = j 
            break
        j += 1
    
    return answer