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

print(len(letsfind)-1)
