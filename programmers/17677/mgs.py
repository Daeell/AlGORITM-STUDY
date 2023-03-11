def solution(str1, str2):

    first = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    second = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    intersection = set(first) & set(second)
    union = set(first) | set(second)

    if len(union) == 0 :
        return 65536
    else :
        inter_cnt = 0
        uni_cnt = 0

        for val in intersection :
            inter_cnt += min(first.count(val), second.count(val))
        for val2 in union :
            uni_cnt += max(first.count(val2), second.count(val2))
        answer = int(inter_cnt/uni_cnt*65536)

    return answer

print(solution(	"aa1+aa2", "AAAA12"))
