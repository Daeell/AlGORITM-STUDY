# 52260	468
import sys
from collections import Counter
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
nlist = [int(input())for _ in range(n)]
nlist.sort()

# 평균 구하기
result = sum(nlist)
print(round(result / len(nlist)))

# 중앙값 구하기
mid = len(nlist) // 2
print(nlist[mid])

# 최빈값 구하기
cnt = Counter(nlist)
most = cnt.most_common()  # 등장 횟수 튜플형식 (숫자, 등장횟수)
appear_num = most[0][1]
mostlist = []

for num in most:
    if num[1] == appear_num:
        mostlist.append(num[0])
if len(mostlist) == 1:
    print(mostlist[0])
else:
    mostlist.sort()
    print(mostlist[1])

# 범위 구하기
print(max(nlist)-min(nlist))
