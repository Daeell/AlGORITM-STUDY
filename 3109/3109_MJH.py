import sys
input = sys.stdin.readline

def find(r, c) -> bool:
    global area, R, DEST, cnt
    if c == DEST:
        cnt += 1
        return True
    if r-1 >= 0 and area[r-1][c+1] == '.':
        area[r-1][c+1] = 'V'
        if find(r-1, c+1):
            return True
            
    if area[r][c+1] == '.':
        area[r][c+1] = 'V'
        if find(r, c+1):
            return True
            
    if r+1 < R and area[r+1][c+1] == '.':
        area[r+1][c+1] = 'V'
        if find(r+1, c+1):
            return True

    return False

def main() -> None:
    global area, R, DEST, cnt
    R, C = map(int, input().split())
    DEST = C-1
    area = []
    for _ in range(R):
        area.append(list(input().strip()))
    
    cnt = 0
    for i in range(R):
        find(i, 0)

    print(cnt)


main()