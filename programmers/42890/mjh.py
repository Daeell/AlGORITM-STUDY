# PASSED
from itertools import combinations
from collections import deque
def solution(relation):
    answer = 0
    col_list = [i for i in range(len(relation[0]))]
    answer_list = deque()
    
    for i in range(1, len(relation[0])+1):
        combi_list = list(combinations(col_list, i))
        
        for combi in combi_list:
            dup_check = set()
            flag = True
            
            for row in range(len(relation)):
                cmp = []
                for col in combi:
                    cmp.append(relation[row][col])
                cmp = tuple(cmp)
                if cmp in dup_check:
                    flag = False
                    break
                else:
                    dup_check.add(cmp)
                    
            if flag == True:
                answer_list.append(set(combi))
    
    # 최소성을 만족시키기 위해, 길이가 짧은 후보 키에서부터 순회하며
    # 자기 자신이 부분 집합이 되는 후보 키를 지워 나갑니다.
    while answer_list:
        answer += 1
        cur = answer_list.popleft()
        new_answer_list = deque()
        for i in range(len(answer_list)):
            if answer_list[i] & cur != cur:
                new_answer_list.append(answer_list[i])
        answer_list = new_answer_list

    return answer