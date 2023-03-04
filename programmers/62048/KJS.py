import math
def solution(w,h):
    w_gcd = w / math.gcd(w,h)
    h_gcd = h / math.gcd(w,h)
    
    if w_gcd > h_gcd:
        answer = w*h - math.ceil(w_gcd/h_gcd) * h_gcd * math.gcd(w,h)
    elif w_gcd < h_gcd:
        answer = w*h - math.ceil(h_gcd/w_gcd) * w_gcd * math.gcd(w,h)
    else:
        answer = w*h - math.gcd(w,h)
    
    
    return answer
