def solution(str1, str2):
    answer = 0
    str1_list = []
    str2_list = []
    for i in range(0,len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i].lower()+str1[i+1].lower())
    for i in range(0,len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append(str2[i].lower()+str2[i+1].lower())
    intersection = []
    for i in str1_list:
        if i in str2_list:
            intersection.append(i)
            str2_list.remove(i)
    a = len(str1_list) + len(str2_list)
    if len(str1_list)==0 and len(str2_list)==0:
        answer = 65536
    else:
        answer=int(len(intersection)/a*65536)
    return answer
