def solution(numbers):
    answer = []
    for num in numbers :
        
        if num == 1 :
            answer.append(2)
            continue
        
        bin_list = list(bin(num)[2:])
        res = ""
        
        if bin_list.count("0") == 0 :
            bin_list[1] = "0"
            bin_list.append("1")
            res = "".join(bin_list)
            answer.append(int(res,2))
            continue
        
        idx = 0
        return_flag = False
        while return_flag != True :
            tmp = bin_list.pop()
            if tmp == "0" :
                bin_list.append("1")
                return_flag = True
            else :
                idx += 1
        
        res = "".join(bin_list)
        
        if idx > 0 :
            res += "0"
            for i in range(idx-1) :
                res += "1"
        answer.append(int(res,2))
                
        
    return answer
