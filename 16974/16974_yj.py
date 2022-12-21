import sys
sys.stdin= open("input.txt", "r")
input = sys.stdin.readline

L, X = map(int, input().split())
dp = [None for _ in range(L)] # dp[level] = 해당 레벨의 버거 



def makeburger(L):
    if L == 0 :
        dp[0] = '1' 
        return dp[0]
    else: 
        if dp[L-1] != None : 
            return dp[L-1]
        else: 
            prevBurger = makeburger(L-1)
            burger = '0'+prevBurger+'1'+prevBurger+'0'
            dp[L-1] = burger
            return dp[L-1]

burger = makeburger(L)
# burgerHeight = len(burger)

ans = 0 
for i in range(X): 
    ans+= int(burger[i])

print(ans)