from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    combi_list = []
    for i in range(1, col +1):
        combi_list.extend(combinations(range(col),i))
    
    answer_list = []
    for i in combi_list:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row: # 유일성 확인
            flag = True

            for j in answer_list:
                if set(j).issubset(set(i)): # 최소성 확인 j가 i의 sub 인지 확인
                    flag = False
                    break

            if flag : answer_list.append(i)


    answer = len(answer_list)
    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))