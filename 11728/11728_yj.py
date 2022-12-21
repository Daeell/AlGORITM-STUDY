import sys
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline

nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
ans = list(A|B)

print(ans)
print(list(A|B).sort)