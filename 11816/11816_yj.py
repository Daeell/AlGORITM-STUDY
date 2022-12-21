import sys
sys.stdin = open("input.txt","r")

def to_decimal(X,Y) :  
    start = len(X)-1
    ans = 0 
    for i in X :
        if Y == 16 : 
            if i == 'a' : 
                i = 10
            elif i == 'b' :
                i = 11
            elif i == 'c' :
                i = 12
            elif i == 'd' :
                i = 13
            elif i == 'e' :
                i = 14
            elif i == 'f' :
                i = 15
        ans += int(i)*(Y**(start))
        start -= 1
    print(ans)

X = input()
if X[0] == '0' :
    if len(X)>=2 and X[1] == 'x' :
        to_decimal(X[2:], 16)
    else : 
        to_decimal(X[1:], 8)
else :
    print(int(X))
