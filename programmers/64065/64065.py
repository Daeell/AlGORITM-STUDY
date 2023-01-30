# st= "{{4,2,3},{3},{2,3,4,1},{2,3}}"

def solution(s):    
    tmp = s[2:-2].split("},{")
    dic = dict()

    for element in tmp :
        for e in element.split(",") :
            if e not in dic :
                dic.setdefault(e, 1)
            else :
                dic[e] +=1 

    answer = list(map(int, sorted(dic, key=lambda x: dic[x], reverse=True)))
    return answer

# solution(st)
