import sys
input = sys.stdin.readline

nums = []
for i in range(5):
    temp = input().split()
    nums.append(temp)

visited = set() 
dx= [-1,1,0,0]
dy= [0,0,-1,1]

# nums[x][y]부터 시작하는 DFS를 구현
def dfs(x,y, num):
    global visited
    num += nums[x][y]
    if len(num)==6 :
        visited.add(num);
        return 
    for i in range(4):
        if x+dx[i]>=0 and x+dx[i]<5 and y+dy[i]>=0 and y+dy[i]<5 :
            dfs(x+dx[i], y+dy[i], num)

for i in range(5):
    for j in range(5):
        num = str()
        dfs(i,j,num)

print(len(visited))
    