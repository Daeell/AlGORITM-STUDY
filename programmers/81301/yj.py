def solution(s):
    answer = ""
    tmp = ""
    nums = ["zero", "one","two","three","four","five","six","seven","eight","nine"]
    for i in range(len(s)) :
        if s[i].isdigit() : 
            answer= answer + s[i]
        else : 
            if len(tmp) == 0 :
                tmp = s[i]
            else: 
                tmp = tmp +  s[i]
        try:
            idx = nums.index(tmp) 
        except ValueError:
            continue
        
        tmp = ""
        answer= answer + str(idx)
    return int(answer)

