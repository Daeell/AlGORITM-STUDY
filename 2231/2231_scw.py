#분해합
import sys
input=sys.stdin.readline

N = input().strip()

if N== 1000000:
    mini = 9*6
else:
    mini = 9* len(N)

N=int(N)

if N-mini <= 0:
    mini = 0
else:
    mini = N-mini

if N == 1:
    print(0)
else:
    for i in range(mini,N):
        ans= start =i
        while 1 :
            for_ans = start % 10
            ans +=for_ans
            if start<10:
                break
            else:
                start = start//10
        if ans == N:
            print(i)
            break
        if i == N-1:
            print(0)

