def solution(today, terms, privacies):
    answer = []
    
    privacies_list = []
    for i in range(len(privacies)):
        info_date, terms_type = privacies[i].split(" ")
        y, m, d = map(int, info_date.split('.'))
        privacies_list.append([i+1, y, m, d, terms_type])
    
    terms_list={}
    for i in range(len(terms)):
        terms_type_1, date = terms[i].split(" ")
        terms_list[terms_type_1] = int(date)
    
    today_ = list(map(int, today.split('.')))
    for info in privacies_list:
        
        # info[2] = info[2]+terms_list[info[-1]]
        # if info[2]>12:
        #     mok=info[2]//12
        #     namuzi = info[2]%12
        #     info[1] = info[1] + mok
        #     info[2] = namuzi
        print(terms_list[info[-1]])
        if info[2] ==12 and terms_list[info[-1]]%12 ==0:
            info[1] = info[1]+terms_list[info[-1]]//12
        else:
            info[2] = info[2]+terms_list[info[-1]]
            mok=info[2]//12
            namuzi = info[2]%12
            info[1] = info[1] + mok
            info[2] = namuzi
        
        if today_[0]>info[1]: # 년이 더 크면
            answer.append(info[0])
        elif today_[0]==info[1]: # 년이 같으면
            if today_[1] > info[2]: # 월이 더 크면
                answer.append(info[0])
            elif today_[1]==info[2]: # 월이 같으면
                if today_[2] >= info[3]: # 일이 더 크거나 같으면
                    answer.append(info[0])

    return answer

print(solution("2022.12.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.12.01 B", "2022.02.19 B", "2022.02.20 C"]))