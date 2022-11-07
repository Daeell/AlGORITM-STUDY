import sys
sys.stdin= open("input.txt", "r")
input = sys.stdin.readline

L, X = map(int, input().split())
dp = [None for _ in range(L)] # dp[level] = 해당 레벨의 버거 

# 대칭이라는 점을 이용해야 할 듯  
def makeburger(L):
    if L == 0 :
        dp[0] = '1' 
        return dp[0]
    else: 
        if dp[L-1] != None : 
            return dp[L-1]
        else: 
            prevBurger = makeburger(L-1)
            burger = '0'+prevBurger + '1'  #반만 저장한다 
            dp[L-1] = burger
            return dp[L-1]

burger = makeburger(L)
# burgerHeight = len(burger)

ans = 0 
for i in range(X): 
    ans+= int(burger[i])

print(ans)