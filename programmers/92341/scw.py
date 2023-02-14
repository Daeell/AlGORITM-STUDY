from collections import defaultdict
import math

def solution(fees, records):
    min_time = fees[0]
    min_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]
    answer = []

    park_info = defaultdict(list)
    for record in records:
        time, num, status = record.split(' ')
        h, m = map(int, time.split(':'))
        park_info[num].append([h*60+m, status])
    

    for keys in park_info:
        if len(park_info[keys]) %2 !=0:
            park_info[keys].append([23*60+59, 'OUT'])
        
        total_time = 0

        for i in range(len(park_info[keys])):
            if i %2 ==0:
                total_time -=park_info[keys][i][0]
            else:
                total_time +=park_info[keys][i][0]
            
        
        if total_time <= min_time:
            answer.append([keys, min_fee])
        else:
            money = math.ceil((total_time-min_time)/per_time) * per_fee + min_fee
            answer.append([keys, money])
    
    answer.sort(key=lambda x: (x[0]))

    real_answer = []
    for i in answer:
        real_answer.append(i[1])
    
    return real_answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

