import sys
from collections import defaultdict
sys.stdin  = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
books = defaultdict(int)
max_num = 0 
for i in range(N):
    book = input().strip()
    books[book]+=1 
    if books[book]> max_num :
        max_num = books[book]

howMany = [[] for i in range(max_num+1)]
for name, num in books.items() :
    howMany[num].append(name)
print(sorted(howMany[-1])[0])
