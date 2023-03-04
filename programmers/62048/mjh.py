# PASSED
def GCD(a, b):
    return a if b == 0 else GCD(b, a%b)
def solution(w,h):
    return w*h-(w+h-GCD(w,h))