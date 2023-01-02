import sys
input = sys.stdin.readline

def check(area) -> bool:
    global jewels
    pass


def cut(imp:tuple, impurities:set, area:list, isRow:bool) -> None:
    global count
    N = len(area)
    impurities.remove(imp)
    if isRow == True:
        row = imp[0]
        for i in range(N):
            if area[row][i] == 2:
                return
            elif area[row][i] == 1:
                impurities.remove((row, i))
            area[row][i] = -1
    else:
        col = imp[1]
        for i in range(N):
            if area[i][col] == 2:
                return
            elif area[i][col] == 1:
                impurities.remove((i, col))
            area[i][col] = -1
    if not len(impurities):
        if check(area):
            count += 1
            return
    else:
        cut(imp, impurities, area, not isRow)


def parse(area:list) -> set:
    impurities = set()
    jewels = set()
    N = len(area)
    for i in range(N):
        for j in range(N):
            if area[i][j] == 1:
                impurities.add((i, j))
            elif area[i][j] == 2:
                jewels.add((i, j))
    return impurities, jewels


def main(N:int) -> int:
    global count, jewels
    count = 0
    area = []
    for _ in range(N):
        area.append(list(map(int, input().split())))
    impurities, jewels = parse(area)
    for imp in impurities:
        cut(imp, impurities, area, True)
        cut(imp, impurities, area, False)
    return count


print(main(int(input().strip())))