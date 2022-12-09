import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().strip())
input_ = list(map(int, input().split()))
del_node = int(input().strip())

in_degree = defaultdict(list)

# 아이디어
#   * 리프 노드는 진입차수가 0개라는 사실을 이용합니다.
#   * 제거하는 노드의 자손 노드들을 모두 찾아들어가서,
#       자식들을 먼저 제거하고 부모를 제거하는 방식인 후위 순회로 제거해줍니다.
#   * 제거하는 데에 사용한 편법으로, 자식을 정말로 제거하는 대신
#       [-1]을 append 해주었습니다.

for cur in range(N):
    parent = input_[cur]
    if parent == -1:
        continue
    in_degree[parent].append(cur)

def delete_children (node):
    if len(in_degree[node]) <= 0:
        in_degree[node] = [-1]
        return
    for child in in_degree[node]:
        delete_children (child)
    in_degree[node] = [-1]

delete_children (del_node)

parent = input_[del_node]
if parent != -1 and len(in_degree[parent]) == 1:
    in_degree[parent] = []

cnt = 0
for i in range(N):
    if len(in_degree[i]) == 0:
        cnt += 1

print(cnt)