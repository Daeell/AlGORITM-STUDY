# PASSED
from collections import defaultdict
def solution(fees, records):
    answer = []
    
    df_time, df_fee, add_time, add_fee = fees
    
    recorder = defaultdict(int)
    parking_lot = dict()
    time_sheet = defaultdict(int)
    for record in records:
        time, number, record_type = record.split(' ')
        h, m = map(int, time.split(':'))
        number = int(number)
        time = h*60 + m
        if record_type == 'IN':
            recorder[number] = time
            parking_lot[number] = True
        else:
            in_time = recorder[number]
            parked_time = time - in_time
            time_sheet[number] += parked_time
            parking_lot[number] = False
    
    tmp_answer = []
    for number in parking_lot:
        parked_time = (23*60+59) - recorder[number] + time_sheet[number] if parking_lot[number] == True else time_sheet[number]
        if parked_time <= df_time:
            tmp_answer.append((number, df_fee))
        else:
            overed_time = parked_time - df_time
            if overed_time%add_time != 0:
                overed_time += add_time - overed_time%add_time
            overed = overed_time // add_time
            tmp_answer.append((number, df_fee + overed*add_fee))
            
    tmp_answer.sort()
    for e in tmp_answer:
        answer.append(e[1])
    
    return answer