import sys
import re
N, K = map(int, sys.stdin.readline().split())
words = []
basic_word = ['a','n','t','i','c']
for i in range(N):
    words.append(list(set(re.sub(r"[a,n,t,i,c]","",(sys.stdin.readline().strip())))))

# print(words)
can_teach = K-5


if K < 5:
    print(0)
