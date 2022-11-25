import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())

time = []
money = []
dp = [0 for _ in range(n+1)]
for _ in range(n):
    t, m = map(int, input().split())
    time.append(t)
    money.append(m)
    # 시간이 퇴사일을 넘기면 일을 하지 않는다.

for today in range(n-1, -1, -1):
    if today + time[today] > n:
        # 해당 일에 근무를 하면 퇴사일을 넘기는지 확인한다.
        # 퇴사일을 넘기면 일을 할 수 없다.
        dp[today] = dp[today+1]
    else:
        # 현재 날짜에서 일을 하지 않는 것이 이득인지 하지 않는 것이 이득인지 고른다.
        dp[today] = max(dp[today+1], money[today] + dp[today + time[today]])

print(dp[0])
