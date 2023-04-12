import sys
sys.stdin = open('python/input.txt', 'r')
input = sys.stdin.readline


# def solution():
#     t = int(input())
#     button = [0, 0, 0]
#     # 300초 60초 10초
#     if t % 10 > 0:
#         return [-1]
#     while t > 0:
#         if t >= 300:
#             button[0] += 1
#             t -= 300
#         elif t >= 60:
#             button[1] += 1
#             t -= 60
#         elif t >= 10:
#             button[2] += 1
#             t -= 10

#     return button

def solution():
    t = int(input())

    btn_time = [300, 60, 10]
    btn_cnt = [0, 0, 0]

    if t % 10 > 0:
        return [-1]

    for i in range(len(btn_time)):
        btn_cnt[i] = t // btn_time[i]
        t %= btn_time[i]

    return btn_cnt


print(*solution())
