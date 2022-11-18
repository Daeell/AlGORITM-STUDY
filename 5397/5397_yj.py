

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def getAnswer() :
    string = input()
    password = [0]
    cursor = 0 
    print(string)
    for i in range(len(string)) : 
        if string[i] == '<' :
            if cursor > 0 :
                cursor -= 1
        if string[i] == '<':
            if cursor < len(password)-1 :  
                cursor += 1 
        if string[i] == '-' :
            password[cursor] = " "
            cursor -= 1
        else : # 문자라면
             password.append(string[i])
             cursor = len(password)-1
    for i in range(len(password)):
        if password[i] != " ":
            print(password[i], end="")


N = int(input())
for i in range(N):
    getAnswer();