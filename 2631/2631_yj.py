import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
seq = [0] # 아이들 줄 번호 (0번 안씀)
dp = [0]*(N+1) # dp 테이블 (0번 안 씀)

for i in range(N):
    seq.append(int(input()))

# LIS 구하기 
dp[1]= 1
for i in range(2, N+1):
    tmp = 0 
    for j in range(1,i): 
        # i보다 작은 수들의 dp값들 중 최댓값을 구한다 
        if seq[j] < seq[i] : 
            #LIS 대상이 될 수 있음 
            tmp = max(tmp, dp[j])
    dp[i] = tmp +1 

# print(dp)
print(N-max(dp))
        

