import sys
sys.stdin = open("input.txt","r")

L = int(input())
words = input()
tmp = '0'
answer = 0 

for i in words :    
    if i.isnumeric() :
        tmp += i 
    else : 
        answer += int(tmp)
        tmp = '0'

if tmp != '0' :
    answer += int(tmp)

print(answer)

# ab 13 c 9 d 07 jeden
# 연속된 숫자는 한 히든 넘버이다.
# 두 히든 넘버 사이에는 글자가 적어도 한 개 있다.
# 히든 넘버는 6자리를 넘지 않는다.
# 모든 히든 넘버의 합을 출력 