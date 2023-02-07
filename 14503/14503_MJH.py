import sys
input = sys.stdin.readline

# area status
#   0 : 청소안된 공간
#   1 : 벽
#   2 : 청소된 공간

def clean(r, c) -> None:
    global area, cnt
    if area[r][c] != 2:
        area[r][c] = 2
        cnt += 1
    return

def search(r, c, d) -> tuple:
    global area
    rotate = {0:3, 3:2, 2:1, 1:0}
    facing = {0:(-1, 0), 3:(0, -1), 2:(1, 0), 1:(0, 1)}
    back = {0:(1, 0), 3:(0, 1), 2:(-1, 0), 1:(0, -1)}

    # 왼쪽으로 돌며 청소할 공간 탐색
    for _ in range(4):
        d = rotate[d]
        if area[r+facing[d][0]][c+facing[d][1]] == 0:
            return (r+facing[d][0], c+facing[d][1], d)
    
    # 후진해야 하는 상황
    if area[r+back[d][0]][c+back[d][1]] != 1:
        return (r+back[d][0], c+back[d][1], d)

    return (-1, -1, -1) # 조건 미충족 시 멈춤

def main():
    global area, cnt
    # begin input
    ROWS, COLUMNS = map(int, input().split())
    r, c, d = map(int, input().split())
    area = []
    for _ in range(ROWS):
        area.append(list(map(int, input().split())))
    # end input

    cnt = 0

    # 멈춤 조건이 발동할 때까지 청소를 진행합니다.
    while d != -1:
        clean(r, c)
        r, c, d = search(r, c, d)

    print(cnt)


main()