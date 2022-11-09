#칸토어 집합
import sys
sys.setrecursionlimit(10**8)

while 1:
    try:
        N=int(input())

        A=["-"]

        if N==0:
            print(A[0])
        # elif N==1:
        #     print(*A,sep="")
        else:
            B=[]
            for i in range(1,N+1):
                B=[" "*(3**(i-1))]                
                A= A + B + A
            print(*A,sep="")

    except ValueError:
        break