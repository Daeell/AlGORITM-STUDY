# N레벨 햄버거의 장 수와 N레벨 패티의 장 수를 계산해서
# nlev_burger, nlev_patty 배열에 저장합니다.
def find_nlev(level, num):
    if level == N+1:
        return
    else:
        nlev_burger.append(num)
        nlev_patty.append(nlev_burger[level-1] + 2)
        find_nlev(level+1, 2*num+3)


# X번째 위치까지 패티가 몇 장 있는지를 구하기 위해
# 이분 탐색으로 찾아 내려갑니다.
def burger(level, start, end):
    global patty_num
    if level == 1:  # 현재레벨이 1레벨이면 끝낸다.
        patty_num += LEVEL_ONE_BURGER[X-start]
        print(patty_num)
        exit(0)

    mid = (start+end)//2
    # Case 1 ~ 3 이면 끝낸다.
    if X == start:   # Case 1: 처음
        print(patty_num)
        exit(0)
    elif X == mid:   # Case 2: 중간
        patty_num += nlev_patty[level-1] + 1
        print(patty_num)
        exit(0)
    elif X == end:   # Case 3: 끝
        patty_num += nlev_patty[level]
        print(patty_num)
        exit(0)

    # Case 4 ~ 5 이면 이분탐색한다.
    elif X < mid:    # Case 4: 처음~중간 사이
        burger(level-1, start+1, mid - 1)
    else:            # Case 5: 중간~끝 사이
        patty_num += nlev_patty[level-1] + 1
        burger(level-1, mid + 1, end-1)


# main
N, X = map(int,input().split())

LEVEL_ONE_BURGER = [0,1,2,3,3]

nlev_burger = [1]
nlev_patty = [1]
patty_num = 0

find_nlev(1, 5)
burger(N, 1, nlev_burger[N])