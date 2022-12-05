import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
children = [0] # 아이들 줄 번호 (0번 안씀)
dp = [[None,None] for _ in range(N+1)]
dp[0]= [0,0] # dp[N] = N명의 아이들이 줄을 설 때 최소로 옮겨야 하는 수 

for i in range(N): 
    children.append(int(input()))


dp[1] = [0, children[1]] # (최소 움직여야 하는 수, 최고 번호)

for i in range(1, N+1): 
    max = dp[i-1][1] 
    if max < children[i]:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = children[i]
    else :  
        dp[i][0] = dp[i-1][0] + 1
        dp[i][1] = max

print(dp)
print(dp[N][0])