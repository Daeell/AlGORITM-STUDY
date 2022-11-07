import sys
from collections import defaultdict
from functools import lru_cache
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n, x = map(int, input().split())

burger = [1]*(n+1)
patt = [1]*(n+1)

for i in range(1, n+1):
    burger[i] = 1 + burger[i-1] + 1 + burger[i-1]+1
    patt[i] = patt[i-1] + 1 + patt[i-1]
