
def solution(s):
    # 48~59 125
    answer = []
    temp=[]
    temp_2=[]
    for i in range (len(s)):
        if 48<=ord(s[i]) <=59:
            if ord(s[i-1]) == 44 or ord(s[i-1]) == 123: 
                temp.append(int(s[i]))
            elif len(temp)>0:
                temp[len(temp)-1]=temp[len(temp)-1]*10 + int(s[i])
        elif ord(s[i])==125 and len(temp)>0:
            temp_2.append(temp)
            temp=[]
    k=1
    while (True):
        for i in temp_2:
            temp_3=set()
            if len(i) == k:
                temp_3 = set(i) - set(answer)
                answer.append(*temp_3)
                k +=1
        if k==len(temp_2)+1:
            break
    return answer
solution("{{20,111},{111}}")