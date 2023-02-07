#패션왕 신해빈
import sys
from collections import defaultdict
input=sys.stdin.readline

N= int(input().strip())

# for _ in range(N):
#     K=int(input().strip())
#     cloth = defaultdict(list)
#     answer=1
#     for _ in range(K):
#         a, b = input().strip().split()
#         cloth[b].append(a)
#     for key in cloth:
#         answer *=(len(cloth[key])+1)
#     print(answer-1)
    
for _ in range(N):
    K=int(input().strip())
    cloth = defaultdict(int)
    answer=1
    for _ in range(K):
        a, b = input().strip().split()
        cloth[b]=cloth[b]+1
    for key in cloth:
        answer *=(cloth[key]+1)
    print(answer -1)
    