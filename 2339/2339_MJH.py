import sys
from collections import defaultdict
input = sys.stdin.readline

def check(area) -> bool:
    pass


def cut_row(idx:int, area_start:tuple, area_end:tuple) -> None:
    global count, area, jewels_row, jewels_col, impurities_rowsort, impurities_colsort
    imp = impurities_rowsort[idx]
    r = imp[0]; c = imp[1]
    for i in range(area_start[0], area_end[0]+1):
        if area[r][i] == 2:
            return
    for i in range()
    cut_col()


def cut_col(imp:tuple, area_start:tuple, area_end:tuple) -> None:
    global count, area, jewels_row, jewels_col, impurities_rowsort, impurities_colsort
    

def parse(area:list):
    impurities = []
    jewels_row = defaultdict(list)
    jewels_col = defaultdict(list)
    N = len(area)
    for i in range(N):
        for j in range(N):
            if area[i][j] == 1:
                impurities.append((i, j))
            elif area[i][j] == 2:
                jewels_row[i].append(j)
                jewels_col[j].append(i)
    return impurities, jewels_row, jewels_col


def main(N:int) -> int:
    global count, area, jewels_row, jewels_col, impurities_rowsort, impurities_colsort
    count = 0
    area = []
    for _ in range(N):
        area.append(list(map(int, input().split())))
    impurities, jewels_row, jewels_col = parse(area)
    impurities_rowsort = sorted(impurities)
    impurities_colsort = sorted(impurities, lambda x: x[1])
    for i in range(len(impurities_rowsort)):
        cut_row(i, (0,0), (N-1,N-1))
    for imp in impurities_colsort:
        cut_col(imp, (0,0), (N-1,N-1))
    return count


print(main(int(input().strip())))