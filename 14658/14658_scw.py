# # 하늘에서 별똥별이 빗발친다
# import sys
# input=sys.stdin.readline

# n, m, l, k = map(int, input().strip().split())
# graph = [[0]*(n+1) for _ in range(m+1)]
# for _ in range(k):
#     x, y = map(int, input().strip().split())
#     graph[y][x]= 1

# def find_star(i,j):
#     cnt = 0
#     visited = [[0]*(n+1) for _ in range(m+1)]
#     for y in range (j, j+l):
#         for x in range (i, i+l):
#             if 0<x<m+1 and 0<y<n+1 and visited[x][y] ==0 and graph[x][y]==1:
#                 cnt +=1
#                 visited[x][y] =1
#     return cnt

# answer = 0
# for i in range(1,m+1-l): # 내부 사각형의 시작 좌표
#     for j in range(1,n+1-l): # 내부 사각형의 시작 좌표
#         answer = max(answer,find_star(i,j)) # 사각형을 기준으로 탐색을 시작

# print(answer)

# 하늘에서 별똥별이 빗발친다
import sys, copy
from collections import defaultdict
input=sys.stdin.readline


def find_star(i,j,star_list,star_list_check,l,n, m):
    cnt = 0
    for y in range (j, j+l):
        for x in range (i, i+l):
            if 0<x<m+1 and 0<y<n+1: 
                if y in star_list[x] and y in star_list_check[x]:
                    cnt +=1
                    a = star_list_check[x].index(y)
                    star_list_check[x][a] =0
    return cnt

def main():
    n, m, l, k = map(int, input().strip().split())
    star_list = defaultdict(list)
    for _ in range(k):
        x, y = map(int, input().strip().split())
        star_list[y].append(x)

    answer = 0
    for i in range(1,m+1-l): # 내부 사각형의 시작 좌표
        for j in range(1,n+1-l): # 내부 사각형의 시작 좌표
            star_list_check = copy.deepcopy(star_list)
            answer = max(answer,find_star(i,j,star_list,star_list_check,l,n, m)) # 사각형을 기준으로 탐색을 시작
    print(answer)

main()