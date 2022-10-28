import sys

def main():
    input = sys.stdin.readline
    def BFS(x, y):
        for i in range(8):
            x_ = x + x_offset[i]
            y_ = y + y_offset[i]
            if 0 < x_ <= W and 0 < y_ <= H:
                if arr[x_][y_] == 1:
                    idx = x_*W + y_
                    if idx not in visited:
                        visited.add(idx)
                        BFS(x_, y_)


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
                idx = i*W + j
                if idx not in visited:
                    visited.add(idx)
                    count += 1
                    BFS(i, j)
        
        print(count)

main()