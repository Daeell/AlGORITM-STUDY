import sys
sys.stdin = open("input.txt","r")
N = int(input())

i= 2 
while (i <= N+1) :
    if (N%i) == 0 :
        print(i)
        N=N/i
        i=2
    else :
        i+=1 