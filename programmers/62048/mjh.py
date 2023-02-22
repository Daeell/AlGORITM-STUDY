# 4, 10, 11, 17, 18번 케이스 시간초과
import sys
sys.setrecursionlimit(10**6)

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)
    
def recur(a, b):
    gcd = GCD(a, b)
    if gcd == 1:
        x, y = 1, 1
        cnt = 1
        while True:
            if x == a and y == b:
                break
            if x < a:
                cnt += 1
                x += 1
                while x > y:
                    cnt += 1
                    y += 1
            if y < b:
                cnt += 1
                y += 1
        return cnt
    
    return gcd*recur(a//gcd, b//gcd)

def solution(w,h):
    answer = w*h - recur(w,h)
    return answer