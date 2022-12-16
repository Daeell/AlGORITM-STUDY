import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
global arr; 
arr = list(map(int, input().split()))


###! 기본 DP LIS 풀이 
# DP = [ 0 for i in range(N)]
# for k in range(N): 
#     DP[k] = 1
#     for i in range(k):
#         if(arr[i] < arr[k]):
#             DP[k] = max(DP[k], DP[i] + 1);
# print(DP[N-1])

###! 이분탐색 LIS 풀이 
def binery_search(k) : 
    l = 0
    r = len(LIS)-1
    mid = (l+r)//2
    # print(LIS)
    # print(arr)
    # print("l=", l,"r=" ,r, "k=",k, "mid=", mid)
    while (l<r):
        if (arr[k]==LIS[mid]): 
            LIS[mid]= arr[k]
            return;
        elif (arr[k]>LIS[mid]) :
            # 무조건 mid 오른쪽에 존재하는 것 
            l = mid+1
        else : 
            # 무조건 mid 왼쪽에 존재하는 것 
            r = mid-1

global LIS 
LIS= []
LIS.append(arr[0])
for k in range(1, N):
    if LIS[-1] < arr[k] :
        LIS.append(arr[k])
    elif LIS[-1] > arr[k] :
        # 이분탐색으로 들어갈 위치를 찾아서 대체한다. 
        binery_search(k)

print(LIS.index(arr[N-1])+1)
