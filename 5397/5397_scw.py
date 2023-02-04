#키 로거
import sys
from collections import deque
input=sys.stdin.readline

N=int(input().strip())

# for _ in range(N):
#     A=[]
#     A=list(input().strip())
#     cnt = 0
#     answer=deque()
#     for i in A:
#         if answer != None:
#             if i == '<':
#                 if len(answer)==0 or cnt ==len(answer)*(-1):
#                     continue
#                 else:
#                     cnt -=1
#             elif i ==">":
#                 if len(answer) ==0 or cnt==0:
#                     cnt=0
#                 else:
#                     cnt +=1
#             elif i == "-":
#                 if len(answer)+cnt<=0:
#                     continue
#                 elif cnt >= 0:
#                     answer.pop()
#                 else:
#                     del answer[len(answer)+cnt-1]
#             else:
#                 answer.insert(len(answer)+cnt,i)
#     print(*answer,sep='')

for _ in range(N):