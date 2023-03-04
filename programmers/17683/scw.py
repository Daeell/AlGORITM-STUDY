#방금그곡
from collections import defaultdict

def solution(m, musicinfos):

    m = m.replace('C#', 'H')
    m = m.replace('D#', 'I')
    m = m.replace('F#', 'J')
    m = m.replace('G#', 'K')
    m = m.replace('A#', 'L')

    answer=defaultdict(list)

    real_answer = '(None)'

    for i in range(len(musicinfos)):
        s,e,title,code = musicinfos[i].split(',')
        s_h, s_m = map(int, s.split(':'))
        e_h, e_m = map(int, e.split(':'))

        times = (e_h*60+e_m) - (s_h*60+s_m)

        code = code.replace('C#', 'H')
        code = code.replace('D#', 'I')
        code = code.replace('F#', 'J')
        code = code.replace('G#', 'K')
        code = code.replace('A#', 'L')
        
        if times >= len(code):
            full_code = code*(times//len(code)) + code[:times%len(code)]
        else:
            full_code = code[:times%len(code)]
        
        if m in full_code:
            answer[times].append(title)

    if len(answer)>0:
        answer_=sorted(answer.items(), reverse=True)
        real_answer = answer_[0][1][0]

    return real_answer

print(solution("ABCDE", ["03:00,03:05,FOO,ABCDEF", "04:00,04:08,BAR,BCD"]))



# def solution(m, musicinfos):

#     m = m.replace('C#', 'H')
#     m = m.replace('D#', 'I')
#     m = m.replace('F#', 'J')
#     m = m.replace('G#', 'K')
#     m = m.replace('A#', 'L')

#     answer_list=[]
#     real_answer = '(None)'
#     for i in range(len(musicinfos)):
#         s,e,title,code = musicinfos[i].split(',')
#         s_h, s_m = map(int, s.split(':'))
#         e_h, e_m = map(int, e.split(':'))

#         times = (e_h*60+e_m) - (s_h*60+s_m)

#         code = code.replace('C#', 'H')
#         code = code.replace('D#', 'I')
#         code = code.replace('F#', 'J')
#         code = code.replace('G#', 'K')
#         code = code.replace('A#', 'L')
        
#         if times >= len(code):
#             full_code = code*(times//len(code)) + code[:times%len(code)]
#         else:
#             full_code = code[:times%len(code)]
        
#         if m in full_code:
#             answer_list.append([times, i, title])

#     if len(answer_list)>1:
#         answer_list.sort(key= lambda x : (-x[0], x[1]))
#         real_answer = answer_list[0][2]
#     elif len(answer_list) == 1:
#         real_answer = answer_list[0][2]
        

#     return real_answer