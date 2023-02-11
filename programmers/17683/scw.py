#방금그곡
import re

def solution(m, musicinfos):
    answer = ''

    fullcode=[]
    for s, e, title, code in musicinfos:
        s_h_m = re.findall(r'\d+', s)
        e_h_m = re.findall(r'\d+', e)
        s_min = s_h_m[0]*60 + s_h_m[1]
        e_min = e_h_m[0]*60 + e_h_m[1]
        fullcode.append([title, (e_min - s_min)*code])

    print(fullcode)

    return answer

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))