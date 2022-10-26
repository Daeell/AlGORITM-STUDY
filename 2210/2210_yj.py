import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

nums = []
for i in range(5):
    temp = input().split()
    nums.append(temp)

visited = set() #[] 리스트를 원소로 갖는 집합

dx= [-1,1,0,0]
dy= [0,0,-1,1]
#x부터 시작하는 DFS를 구현, 단 visited는 6번째 숫자일 때만 기록
current_visit= tuple()
def dfs(x,y):
    global visited, current_visit
    current_visit.append(nums[x][y])
    if len(current_visit)==6 :
        visited.add(current_visit);
        current_visit=[] # 초기화
        return 
    for i in range(4):
        dfs(x+dx[i], y+dy[i])

for i in range(5):
    for j in range(5):
        current_visit.append(nums[i][j])
        dfs(i,j)

print(len(visited))
    
