import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
words = [input().rstrip()[4:-4] for _ in range(n)]
# ['rc', 'hello', 'car']
visited = [0] * 27
cnt = 0
must = [ord("a")-97, ord("n")-97, ord("t")-97, ord("i")-97, ord("c")-97]
# [0, 13, 19, 8, 2]
for m in must:
    visited[m] = 1
remain = [i for i in range(27)]
for j in must:
    remain.remove(j)

if k >= 5:
    remain_comb = list(combinations(remain, k-5))

for know in remain_comb:
    for i in know:
        visited[i] = 1
    for word in words:
        for i in range(len(word)):
            if visited[ord(word[i])] == 0:
                break
