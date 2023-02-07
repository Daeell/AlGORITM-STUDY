import sys
from collections import defaultdict
import itertools

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    clothes = []
    for _ in range(N):
        clothes.append(tuple(map(str, sys.stdin.readline().split())))

    Dictclothes = defaultdict(list)

    for v, k in clothes:
        Dictclothes[k].append(v)
    
    print(Dictclothes)


# Ndict = defaultdict(list)
# for v,k in N:
#     Ndict[k].append(v)
