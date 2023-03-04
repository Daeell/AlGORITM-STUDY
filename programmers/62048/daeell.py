import math


def solution(w, h):
    # 최대 공약수 계산
    gcd = math.gcd(w, h)

    # 사용 가능한 정사각형 개수 계산
    answer = w * h - ((w + h) - gcd)

    return answer
