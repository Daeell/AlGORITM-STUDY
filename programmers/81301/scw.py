from collections import deque

def solution(s):
    answer = ''

    s = deque(s)
    while s:
        temp = s.popleft()
        if ord(temp) >=58:
            if temp == 'o':
                answer +='1'
                s.popleft()
                s.popleft()
            elif temp == 't':
                temp = s.popleft()
                if temp == 'w':
                    answer+='2'
                    s.popleft()
                else : 
                    answer+='3'
                    s.popleft()
                    s.popleft()
                    s.popleft()
            elif temp == 'f':
                temp = s.popleft()
                if temp=='o':
                    answer+='4'
                    s.popleft()
                    s.popleft()
                else:
                    answer+='5'
                    s.popleft()
                    s.popleft()
            elif temp =='s':
                temp = s.popleft()
                if temp =='i':
                    answer+='6'
                    s.popleft()
                else:
                    answer+='7'
                    s.popleft()
                    s.popleft()
                    s.popleft()
            elif temp=='e':
                answer+='8'
                s.popleft()
                s.popleft()
                s.popleft()
                s.popleft()
            elif temp =='n':
                answer+='9'
                s.popleft()
                s.popleft()
                s.popleft()
            elif temp =='z':
                answer +='0'
                s.popleft()
                s.popleft()
                s.popleft()
        else:
            answer +=temp


    answer = int(answer)
    return answer


print(solution("one4seveneighttwothreefourfivesixseveneightninezero"))