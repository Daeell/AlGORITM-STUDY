def solution(s):
    answer = 0
    k=len(s)//2 # 최대 중복가능한 길이

    temp_list=[]
    temp_list_2=[]
    for a in range(1, k+1):
        for i in range(len(s)):
            temp = s[i:i+a]
            for j in range(i+1, len(s)):
                x = s[j:j+a]
                if temp == x:
                    temp_list.append(temp)
                else:
                    print(s[j-a:j])
                    if len(temp_list)>0:
                        temp_list_2.extend([len(temp_list)+1,temp_list[0]])
                        temp_list=[]
                    elif temp != s[j-a:j]:
                        temp_list_2.extend([temp])
                        temp_list=[]
                    break

    return answer

print(solution("aabbaccc"))