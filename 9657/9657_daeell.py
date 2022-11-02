
import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
dp = {i: False for i in range(1, n+1)}


def game():
    dp[1] = True
    dp[3] = True
    dp[4] = True
    dp[5] = True

    for i in range(6, n+1):
        if(dp[i-1] and dp[i-3] and dp[i-4] and dp[i-5]):
            dp[i] = True
        else:
            dp[i] = False


game()
if dp[n] == True:
    print('SK')
else:
    print('CY')
