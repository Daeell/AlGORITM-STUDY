#소인수분해
import sys
input=sys.stdin.readline

N= int(input().strip())

a=2
while 1:
    if N%a ==0:
        print(a)
        N=N//a
    elif N==1:
        break
    else:
        a+=1

