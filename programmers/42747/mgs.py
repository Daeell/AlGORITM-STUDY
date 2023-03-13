def solution(citations):
    
    
    # 이분탐색으로 풀면 안되는 이유 : h의 최댓값이 list내의 값이 아닐 수 있음
    # 예시 : [6, 5, 5, 5, 3, 2, 1, 0] 에서 답은 '3'이 아닌 '4'임
    # citations.sort()
    # # print(citations)
    
    # start = 0
    # end = len(citations) - 1
    # _max = 0
    # while start <= end :
    #     mid = (start + end) // 2
    #     over = [x for x in citations if x >= citations[mid]]
        
    #     if len(over) < citations[mid] :
    #         start = mid + 1
    #     else :
    #         end = mid - 1
    #         _max = max(_max, citations[mid])
    # answer = _max
    # return answer

    citations.sort(reverse=True)
    tmp = []
    for idx, val in enumerate(citations, start = 1) :
        tmp.append(min(idx, val))
    return max(tmp)
        

print(solution([3, 0, 6, 1, 5]))
