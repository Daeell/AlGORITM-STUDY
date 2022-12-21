#배열 합치기
import sys
input=sys.stdin.readline

n, k =map(int, input().strip().split())

A=[]
for _ in range(2):
    A.extend(map(int, input().strip().split()))

print(*sorted(A),sep=' ')