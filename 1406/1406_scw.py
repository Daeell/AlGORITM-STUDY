# #에디터
# import sys
# input=sys.stdin.readline

# string = list(input().strip())
# n = int(input().strip())
# cursor =len(string)
# for _ in range(n):
#     cmd = input().strip()
#     if cmd[0:1] == 'P':
#         _, ip = cmd.split()
#         string.insert(cursor,ip)
#         cursor +=1
#     elif cmd[0:1] == "L":
#         if cursor ==0:
#             continue
#         else:
#             cursor -=1
#     elif cmd[0:1] == "D":
#         if cursor == len(string):
#             continue
#         else:
#             cursor +=1
#     else:
#         if cursor ==0:
#             continue
#         del string[cursor-1]
#         cursor -=1

# print(*string,sep="")

#에디터
import sys
input=sys.stdin.readline

Left = list(input().strip())
Right=[]
n = int(input().strip())
cursor =len(Left)
for _ in range(n):
    cmd = input().strip()
    if cmd[0:1] == "P":
        _, ip = cmd.split()
        Left.append(ip)
    elif cmd[0:1] == "L":
        if len(Left)==0:
            continue
        else:
            Right.append(Left.pop())
    elif cmd[0:1] == "D":
        if len(Right) ==0:
            continue
        else:
            Left.append(Right.pop())
    else:
        if len(Left) == 0:
            continue
        Left.pop()
sorted(Right,reverse=True)
result = Left + Right
print(*result,sep="")

