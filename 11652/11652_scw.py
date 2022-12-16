# 카드
import sys
from collections import defaultdict
input=sys.stdin.readline

N = int(input().strip())

count = defaultdict(int)
answer = sys.maxsize
answer_val =0
for i in range(N):
    a = int(input().strip())
    count[a] +=1
    if count[a] > answer_val:
        answer_val = count[a]
        answer = a
    elif count[a] == answer_val:
        if answer > a:
            answer = a


print(answer)