import sys
input = sys.stdin.readline

def main(N):

    def area_check(begin_x, end_x, begin_y, end_y):
        imp_cnt = 0
        jewel_cnt = 0
        for i in range(begin_x, end_x+1):
            for j in range(begin_y, end_y+1):
                if area[i][j] == 1:
                    imp_cnt += 1
                elif area[i][j] == 2:
                    jewel_cnt += 1
        return imp_cnt, jewel_cnt

    def cut_row(r, begin, end):
        # If row is on the edge of the area, return 0.
        if r == begin[0] or r == end[0]:
            return 0
        # If the jewel is on the row, return 0.
        for i in range(begin[1], end[1]+1):
            if area[r][i] == 2:
                return 0
        # Check the area.
        above_imp, above_jwl = area_check(begin[0], r-1, begin[1], end[1])
        below_imp, below_jwl = area_check(r+1, end[0], begin[1], end[1])
        if not above_jwl or not below_jwl:
            return 0
        if above_jwl <= above_imp or below_jwl <= below_imp:
            return 0
        if above_jwl == 1 and below_jwl == 1 and above_imp == 0 and below_imp == 0:
            return 1
        else:
            above_cnt = 1 if above_imp == 0 and above_jwl == 1 else 0
            below_cnt = 1 if below_imp == 0 and below_jwl == 1 else 0
            if above_jwl > 1:
                for c in range(begin[1], end[1]+1):
                    above_cnt += cut_col(c, begin, (r-1, end[1]))
            if below_jwl > 1:
                for c in range(begin[1], end[1]+1):
                    below_cnt += cut_col(c, (r+1, begin[1]), end)
            return above_cnt * below_cnt

    def cut_col(c, begin, end):
        # If column is on the edge of the area, return 0.
        if c == begin[1] or c == end[1]:
            return 0
        # If the jewel is on the column, return 0.
        for i in range(begin[0], end[0]+1):
            if area[i][c] == 2:
                return 0
        # Check the area.
        above_imp, above_jwl = area_check(begin[0], end[0], begin[1], c-1)
        below_imp, below_jwl = area_check(begin[0], end[0], c+1, end[1])
        if not above_jwl or not below_jwl:
            return 0
        if above_jwl <= above_imp or below_jwl <= below_imp:
            return 0
        if above_jwl == 1 and below_jwl == 1 and above_imp == 0 and below_imp == 0:
            return 1
        else:
            above_cnt = 1 if above_imp == 0 and above_jwl == 1 else 0
            below_cnt = 1 if below_imp == 0 and below_jwl == 1 else 0
            if above_jwl > 1:
                for r in range(begin[0], end[0]+1):
                    above_cnt += cut_row(r, begin, (end[0], c-1))
            if below_jwl > 1:
                for r in range(begin[0], end[0]+1):
                    below_cnt += cut_row(r, (begin[0], c+1), end)
            return above_cnt * below_cnt

    cnt = 0
    area = []
    for _ in range(N):
        area.append(list(map(int, input().split())))
    for r in range(N):
        cnt += cut_row(r, (0,0), (N-1, N-1))
    for c in range(N):
        cnt += cut_col(c, (0,0), (N-1, N-1))
    return cnt if cnt else -1

print(main(int(input().strip())))