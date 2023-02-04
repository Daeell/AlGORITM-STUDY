import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
stars = []
ans = 0
cnt = 0
tmp = 0

for _ in range(k):
    x, y = map(int, input().split())
    stars.append([x, y])

for i in range(k):
    nx = stars[i][0]
    ny = stars[i][1]

    if (nx+l) <= n & (ny+l) <= m:
        for j in range(k):
            if nx <= stars[j][0] <= nx+l & ny <= stars[j][1] <= ny+l:
                tmp += 1
        cnt = max(cnt, tmp)
        tmp = 0
    if (nx+l) <= n & (ny-l) >= 0:
        for j in range(k):
            if nx <= stars[j][0] <= nx+l & ny-l <= stars[j][1] <= ny:
                tmp += 1
        cnt = max(cnt, tmp)
        tmp = 0
    if (nx-l) >= 0 & (ny-l) >= 0:
        for j in range(k):
            if nx-l <= stars[j][0] <= nx & ny-l <= stars[j][1] <= ny:
                tmp += 1
        cnt = max(cnt, tmp)
        tmp = 0
    if (nx-l) >= 0 & (ny+l) <= m:
        for j in range(k):
            if nx-l <= stars[j][0] <= nx & ny <= stars[j][1] <= ny+l:
                tmp += 1
        cnt = max(cnt, tmp)
        tmp = 0
    ans = max(ans, cnt)

print(ans)
