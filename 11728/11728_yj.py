import sys
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline

nA, nB = map(int, input().split())
A = input().split() + input().split()

ans = list(map(int, A))
ans.sort()
print(*ans, sep=" ")