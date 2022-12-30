import sys
from collections import Counter
sys.stdin = open('python/input.txt', 'r')
input = sys.stdin.readline

N = int(input())
cnt = 0
# 길이와 해당 숫자, 마지막 숫자 3차원 배열의 dp를 만든다.
dp = [[[0 for length in range(N+1)]
       for first in range(10)] for last in range(10)]

# 해당 길이에서 해당 숫자가 계단 수라면 체크를 해두고, 해당 숫자의 마지막 숫자를 저장해둔다.
# 그러면 먼저 해당 length에서 number를 늘려준다.
# 1. length-1의 상황에서 해당 number에서 해딩 last가 1인 경우
# 2. last보다 +=1이거나 -=1일 경우 cnt +=1을 해준다.
# 3. 그러면 해당 숫자를 확인하는 방법은 뭘까.. 그걸 모두 확인할 수 없으니 해당 길이에서 첫번째 숫자랑 마지막 숫자만 확인하자 어차피 2자리 숫자부터 확인하자나 그러니까 만약 2자리 숫자일 때 계단 수면 3자리 숫자일때 마지막 숫자랑 비교해서 계단 수면 계단 수가 될 거고 그 이후부터 사이에 무슨 숫자가 들어오건 상관이 없잖아.

for first in range(1, 10):
    for last in range(0, 10):
        if first - last == 1 or first - last == -1:
            dp[2][first][last] = 1


for length in range(3, N+1):
    for first in range(1, 10):
        for last in range(0, 10):
            if dp[length-1][first][last] == 1 and last - 1 >= 0:
                dp[length][first][last-1] == 1
            elif dp[length-1][first][last] == 1 and last + 1 <= 9:
                dp[length][first][last+1] == 1
