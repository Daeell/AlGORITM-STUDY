# # 가장 긴 증가하는 부분 수열 2
# import sys
# input=sys.stdin.readline

# def binary_search(dp,value):
#     s= 0
#     e = len(dp)-1
#     while (s<e):
#         mid = (s+e)//2
#         if value>dp[mid]:
#             s = mid+1
#         else:
#             e= mid
#     return (s+e)//2

# def main():
#     N = int(input().strip())
#     A = list(map(int,input().strip().split()))
#     dp=[]
#     for i in range(N):
#         if i==0:
#             dp.append(A[i])
#         elif A[i] > dp[-1]:
#             dp.append(A[i])
#         else:
#             idx = binary_search(dp, A[i])
#             dp[idx] = A[i]

#     print(len(dp))

# main()

# 가장 긴 증가하는 부분 수열 2
import sys
from bisect import bisect_left
input=sys.stdin.readline

def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    dp=[]
    dpL=0
    for i in range(N):
        if i==0:
            dp.append(A[i])
            dpL+=1
        elif A[i] > dp[-1]:
            dp.append(A[i])
            dpL+=1
        else:
            dp[bisect_left(dp, A[i])] = A[i]

    print(dpL)

main()