import sys
from collections import deque
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
N += 1; M += 1; L += 1

meteor = []

for _ in range(K):
    x, y = map(int, input().split())
    meteor.append((x, y))

meteor.sort()

# begin find
maximum = 0
for i in range(K):
    x_range = []

    for j in range(i, K):
        if meteor[i][0]+L < meteor[j][0]:
            break
        x_range.append(meteor[j])

    x_range.sort(key=lambda x: x[1])
    
    y_range = deque()
    for j in range(len(x_range)):
        y_range.append(x_range[j])
        if y_range[0][1]+L < x_range[j][1]:
            y_range.popleft()
        if len(y_range) > maximum:
            maximum = len(y_range)

print(K-maximum)
