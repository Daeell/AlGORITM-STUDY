# 트리
import sys
from collections import defaultdict
input=sys.stdin.readline

N = int(input().strip())
temp = list(map(int, input().strip().split()))
del_node = int(input().strip())
tree = defaultdict(list)

for i in range(N):
    if i == del_node:
        continue
    tree[temp[i]].append(i)


def del_node_tree(delete_node):
    if len(tree[delete_node]) ==0:
        tree[delete_node] = None
        return
    elif len(tree[delete_node]) ==1:
        del_node_tree(tree[delete_node][0])
        tree[delete_node]=None
    else:
        del_node_tree(tree[delete_node][0])
        del_node_tree(tree[delete_node][1])
        tree[delete_node]=None

del_node_tree(del_node)

cnt=0
for i in range(N):
    if tree[i] !=None and (len(tree[i])==0):
        cnt+=1

print(cnt)