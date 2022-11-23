import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))
costs = [[0]*n for i in range(n)]

# dp 테이블을 만들어서 해당 도시에서 각 도시로 가는 기름 값을 구한다.
# 각 테이블의 행에서 최솟값의 기름이 있으면 그걸로 대체한다.
print(costs)
