#계단수
import sys
from itertools import permutations
input=sys.stdin.readline


Word_length= int(input().strip())

if Word_length <=9:
    print(0)
else:
    a = Word_length
    answer=0
    temp = '1'+'0'*(a-1)
    if len(set(list(temp)))==0:
        for N in permutations(list(temp),a):
            while len(N)==a:
                dp=[0]*(a)
                cnt=0
                for i in range(1,a):
                    if abs(int(N[i])-int(N[i-1])) == 1:
                        if N[i-1] == '0' and N[i-2] == '1':
                            cnt=1
                            dp[i] = dp[i-1]+cnt
                        elif int(N[i-1]) != 0:
                            cnt +=1
                            dp[i] = dp[i-1]+cnt
                    else:
                        cnt=0
                        dp[i]=dp[i-1]
                N = str(int(N)+1)
                print(N)
                answer = answer + dp[a-1]
    print(answer%1000000000)