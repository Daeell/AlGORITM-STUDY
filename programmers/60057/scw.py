def solution(s):
    answer = 1001
    k = len(s)//2+1

    if len(s) ==1 :
        return 1

    
    for i in range(1, k):
        temp = s[:i]
        cnt =1
        temp_list=[]
        for j in range(i, len(s), i):
            curr = s[j:j+i]
            if temp == curr:
              cnt +=1
            else:
                if cnt >1:
                    temp_list.extend([str(cnt)])
                temp_list.extend([temp])
                cnt=1
                temp = curr
        if cnt >1:
            temp_list.extend([str(cnt)])
        temp_list.extend([temp])

        answer = min(answer, len(''.join(temp_list)))

    return answer

print(solution("a"))