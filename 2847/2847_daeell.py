import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
stk = [int(input()) for _ in range(n)]
big = stk.pop()
ans = 0

# 반복문을 돌면서 pop을 한다.
# pop한 값을 별도의 변수에 저장해준다.
# 다음에 pop한 값과 비교한다.
# 다음에 pop한 값이 더 작아지도록 숫자를 뺀다.
while stk:
    small = stk.pop()
    if small >= big:
        ans += small-big+1
        big = big - 1
    else:
        big = small
print(ans)
