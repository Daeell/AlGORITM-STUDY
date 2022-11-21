import sys
from collections import defaultdict
from itertools import combinations
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    clothes = []
    f_c = []
    n = int(input())
    for i in range(1, n+1):
        fashion, kind = input().split()
        clothes.append((kind, fashion))

    for i in range(1, len(clothes)+1):
        f_c.append(list(combinations(clothes, i)))
    print(f_c)

    for c in f_c:
        for i in range(len(c)):

            # 조합을 구할 때에는 kind가 겹치는 것이 들어가서는 안된다.
