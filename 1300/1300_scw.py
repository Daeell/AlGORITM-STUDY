# k번째 수
import sys
input=sys.stdin.readline

N = int(input().strip())
K = int(input().strip())

s = 1
e = K
answer =0
while s <= e:
    cnt =0
    mid = (s+e)//2
    for i in range(1, N+1):
        cnt += min(mid//i, N)
    
    if cnt >= K:
        answer = mid
        e = mid -1
    else:
        s = mid + 1

print(answer)