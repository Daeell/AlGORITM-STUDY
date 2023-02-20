# PASSED
import sys
sys.setrecursionlimit(10**6)
def solution(m, n, puddles):
    arr = [[0 for _ in range(m)] for _ in range(n)]
    
    if puddles != []:
        for y, x in puddles:
            arr[x-1][y-1] = -1
        
    arr[n-1][m-1] = 1
    
    def recur(x, y):
        if arr[x][y] == 0:
            if x+1 < n and arr[x+1][y] != -1:
                arr[x][y] = (arr[x][y] + recur(x+1, y))%1000000007
            if y+1 < m and arr[x][y+1] != -1:
                arr[x][y] = (arr[x][y] + recur(x, y+1))%1000000007
        return arr[x][y]%1000000007
    
    return recur(0, 0)