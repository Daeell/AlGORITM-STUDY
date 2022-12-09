import sys
from collections import defaultdict
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
N = int(input())
graph = defaultdict(set) # (부모, 자식1, 자식2) - 순서는 상관없음 

arr = list(map(int, input().split()))
# delnode = set()
# delnode.add(int(input()))
delnode= int(input())

for i in range(N): 
    # parent = arr[i]
    # if i in delnode :  # 내가 삭제 노드라면 
    #     continue
    # elif parent in delnode : # 내 부모가 삭제 노드라면 
    #     delnode.add(i) 
    #     continue 
    graph[arr[i]].add(i) # 부모 노드에 나를 추가 
    graph[i].add(arr[i]) # 나에게 부모 노드를 추가 

parent = arr[delnode]
graph[parent].remove(delnode)
graph[delnode].remove(parent)

print(graph)

########### 그래프 완성

# ans = 0
# for i in range(N) :
#     if len(graph[i]) == 1 :
#         ans+=1 
#     print(i, len(graph[i]))
# print(ans)



### 비연결 요소도 고려하기 