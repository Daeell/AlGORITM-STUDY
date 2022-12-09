import sys
from collections import defaultdict
N = int(sys.stdin.readline())
root_input = list(map(int, sys.stdin.readline().split()))
select = int(sys.stdin.readline())
root_input_enum = list(enumerate(root_input))

tree = defaultdict(list)
for node,i in root_input_enum:
    root = i
    if root == -1:
        continue
    else:
        if node % 2 == 1:
            tree[root].append(node)
        elif node % 2 == 0:
            tree[root].append(node)


for i in range(N):
    if i >= select and i in tree:
        del tree[i]
    else:
        continue
        
print(len(tree))
