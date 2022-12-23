# #문자열 폭발
# import sys
# input=sys.stdin.readline

# string = input().strip()

# bomb = input().strip()

# while 1:
#     if bomb in string:
#         string = string.replace(bomb, '')
#     elif len(string) ==0:
#         print("FRULA")
#         break
#     else:
#         print(string)
#         break

# #문자열 폭발
# import sys
# from collections import deque
# input=sys.stdin.readline

# left = deque(input().strip())
# right =deque()
# bomb = list(input().strip())

# for i in range(len(bomb)):
#     right.append(left.pop())

# a = len(left)
# for i in range(a):
#     right.append(left.pop())
#     if list(right)[-1:-len(bomb)-1:-1] == bomb:
#         for _ in range(len(bomb)):
#             right.pop()


# if len(right)==0:
#     print("FRULA")
# else:
#     right.reverse()
#     print(*right,sep="")

#문자열 폭발
import sys
from collections import deque
input=sys.stdin.readline

left = deque(input().strip())
right =[]
bomb = list(input().strip())

a = len(left)
b = len(bomb)

for i in range(a):
    a= left.popleft()
    if b == 1 and [a] == bomb:
        continue
    elif len(right) >=b-1 and right[-b+1:]+[a]==bomb:
        for _ in range(b-1):
            right.pop()
    else:
        right.append(a)

if right:
    print(*right,sep="")
else:
    print("FRULA")
    