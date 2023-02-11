# 정확성 15, 19 / 효율성 4 실패
from collections import defaultdict

def solution(phone_book):
    answer = True

    dic = defaultdict(str)
    
    for i in range(len(phone_book)):
        s = phone_book[i]
        if dic[s[0]]:
            cmp = dic[s[0]]
            flag = True
            for j in range(min(len(cmp), len(s))):
                if cmp[j] != s[j]:
                    flag = False
                    break
            if flag == True:
                answer = False
                break
        else:
            dic[s[0]] = s

    return answer

print(solution(["119", "97674223", "1195524421"]))