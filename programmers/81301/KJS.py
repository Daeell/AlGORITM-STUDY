def solution(s):
    answer = ''
    number_str=['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number_int=['0','1','2','3','4','5','6','7','8','9']
    s_list = list(s)
    res = []
    for i in range(len(s_list)):
        if s_list[i] in number_int:
            res.append(s_list[i])
        else:
            answer += s_list[i]
            if answer in number_str:
                answer_int = number_str.index(answer)
                res.append(str(answer_int))
                answer =''
        
    return int(''.join(res))
