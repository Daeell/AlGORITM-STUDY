#8진수, 10진수, 16진수
import sys
input=sys.stdin.readline

N = input().strip()

if '0x' == N[0:2]:
    print(int(N,16))
elif '0' == list(N)[0]:
    print(int(N,8))
else:
    print(int(N))