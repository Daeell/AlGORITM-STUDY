#모든 순열
import sys
from itertools import permutations
input=sys.stdin.readline

N= int(input().strip())

A=[ i for i in range(1,N+1)]

for perm in permutations(A):
    print(*perm,sep=" ")