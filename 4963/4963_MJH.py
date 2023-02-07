import sys
sys.setrecursionlimit(10**6)

def main():
    def DFS(x, y):
        for i in range(8):
            x_ = x + x_offset[i]
            y_ = y + y_offset[i]
            if 0 <= x_ < H and 0 <= y_ < W:
                if arr[x_][y_] == '1':
                    if (x_,y_) not in visited:
                        visited.add((x_,y_))
                        DFS(x_, y_)

    input = sys.stdin.readline
    answer = []
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0: break
        
        arr = [0]*H
        for i in range(H):
            arr[i] = input().split()

        x_offset = [-1, 0, 0, 1, -1, -1, 1, 1]
        y_offset = [0, 1, -1, 0, -1, 1, -1, 1]
        visited = set()
        count = 0

        for i in range(H):
            for j in range(W):
                if arr[i][j] == '1':
                    if (i,j) not in visited:
                        visited.add((i,j))
                        count += 1
                        DFS(i, j)
        
        answer.append(count)

    for i in range(len(answer)):
        print(answer[i])

main()