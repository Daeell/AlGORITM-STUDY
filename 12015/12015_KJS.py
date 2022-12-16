import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

letsfind = [0]

for a in A:
    if letsfind[-1] < a:
        letsfind.append(a)
    elif letsfind[-1] > a:
        idx = bisect_left(letsfind,a)
        letsfind[idx] = a

if letsfind[0] == 0:        # 앞에 넣었던 0이 0이면 삭제를 진행 
    del letsfind[0]

print(len(letsfind))

# print(letsfind)  # 수열 출력까지 가능한것으로 보임
