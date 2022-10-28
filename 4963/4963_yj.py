import sys
from collections import deque
sys.stdin = open("input.txt","r")
input = sys.stdin.readline


def bfs(p,q, island) :
    dx = [0,0,-1,-1,-1,1,1,1]
    dy = [-1,1,-1,0,1,-1,0,1]

    # p,q 방문처리
    island.remove((p,q))
    for i in range(8):
        if p+dx >=0 and p+dx <w and q+dy>=0 and q+dy <h :


def do_each(w,h) :
    mat = []
    island= set()
    for i in range(h):
        tmp = input().strip().split()
        mat.append(input().strip().split())
        for j in range(j) :
            if tmp[i][j] == '1' : #섬이면 따로 섬의 집합을 만들어 둔다
                island.add((i,j))
    # 아무 섬(1)에서나 bfs 시행
    # 방문할 때마다 island 목록에서 지우고, 모든 방문이 끝났을 때 방문하지 않은 섬이 있다면 섬의 갯수를 +1 하고 다시 bfs
    cnt = 0 #섬 갯수 
    while len(island) != 0 :
        for p,q in island :
            bfs(p,q, island)
            break
    
    print(cnt) #섬의 갯수 출력 
        
while True: 
    w, h = map(int, input().strip().split())
    if w==0 and h ==0 :
        break
    else :
        do_each(w,h)

    
