# 돌 게임 3
import sys
input=sys.stdin.readline

N= int(input().strip())

cnt =0

dp = [[0]*(N*3) for _ in range(N)]
sele = [1,3,4]

dp[0]=1
def find_winner(N, cnt):
    if N<=2:
        return N
    else:
        dp[1]=1
        dp[2]=2
        nums=[1,3,4]   
        for i in range(N):
            k=i
            while k<=0:
                for sel in nums:
                    if k - sel == 0:
                        cnt+=1
                        break
                    elif k - sel>=0:
                        k=k-sel
                        cnt+=1
    return cnt

if find_winner(N,cnt) %2 ==0:
    print("SK")
else:
    print("CY")