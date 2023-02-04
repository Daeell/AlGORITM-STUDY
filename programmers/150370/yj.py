import datetime as dt

# t0 + relativedelta(months=2)

def solution(today, terms, privacies):
    termsDic= {}
    privDic = {}
    destruction = {}
    FORMAT = '%Y.%m.%d'
    today = dt.datetime.strptime(today, FORMAT)

    for t in terms :
        tmp = t.split()
        termsDic[tmp[0]] = int(tmp[1])
    for p in privacies :
        tmp = p.split()
        privDic[tmp[1]] = tmp[0]
        tmpMonth = int(tmp[0][5:7])+ termsDic[tmp[1]]
        if tmpMonth <= 12 : 
            # 해는 그대로
            destruction = tmp[0][0:4] +"-"+  "{:02d}".format(tmpMonth) +"-"+ tmp[0][8:] 
        else : 
            # 해 더하고 연 빼고 
            destruction = str(int(tmp[0][0:4])+1) +"-"+ "{:02d}".format(tmpMonth-12)  + "-"+ tmp[0][8:]
        

        print("파기 날짜" , destruction)
        # 왜 아래에서 function missing required argument 'year' (pos 1) 에러 나는거죠..?
        print("파기 날짜" , dt.datetime().strptime(destruction, '%Y-%m-%d'))
        # print(dt.datetime.strptime("2017-01-02 14:44", "%Y-%m-%d %H:%M"))

        # privDic[tmp[1]] = dt.datetime.strptime(tmp[0], FORMAT)
        
        # print("due는 ", due)
        
        
        
    print( today, termsDic, privDic)
    # date+timedelta(days=35)
    
    answer = []
    return answer

solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])