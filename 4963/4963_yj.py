import sys
from collections import deque
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

def bfs(p,q, island, visited) :
    dx = (0,0,-1,-1,-1,1,1,1)
    dy = (-1,1,-1,0,1,-1,0,1)
    # p,q 방문처리
    queue = deque()
    queue.append((p,q))
    visited.add((p,q))
    while len(queue) != 0 :
        p,q = queue.popleft()
        island.remove((p,q)) 
        for i in range(8):
            if p+dx[i] >=0 and p+dx[i] <h and q+dy[i]>=0 and q+dy[i] <w :
                if (p+dx[i], q+dy[i]) in island and (p+dx[i],q+dy[i]) not in visited :
                    queue.append((p+dx[i],q+dy[i])) # 인큐
                    visited.add((p+dx[i],q+dy[i]))

def do_each(w,h) :
    mat = []
    island= set()
    for i in range(h):
        tmp = input().strip().split()
        mat.append(tmp)
        for j in range(w) :
            if tmp[j] == '1' : #섬이면 따로 섬의 집합을 만들어 둔다
                island.add((i,j))
    cnt = 0 #섬 갯수 
    visited = set()
    while len(island) != 0 :
        cnt += 1 
        for p,q in island :
            bfs(p,q, island, visited)
            break
    print(cnt) #섬의 갯수 출력 
        
while True: 
    w, h = map(int, input().strip().split())
    if w==0 and h ==0 :
        break
    else :
        do_each(w,h)