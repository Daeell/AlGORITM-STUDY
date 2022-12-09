# 30616	36
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
nodes = list(map(int, input().split()))
d_node = int(input())
deleted = -2
cnt = 0


def deep_del(number):
    while(1):
        # 그 값을 가진 노드가 리스트에 없을 때까지 제거한다.
        if number in nodes:
            idx = nodes.index(number)
            nodes[idx] = deleted
            deep_del(number)
            # 노드의 값을 가진 노드(자식노드)를 제거한다.
            deep_del(idx)
        else:
            break


nodes[d_node] = deleted
deep_del(d_node)

for i in range(len(nodes)):
    # i번째 노드가 삭제되지 않고 그 값을 가진 노드가 없다면 (=자식노드가 없다면)
    if nodes[i] != deleted and i not in nodes:
        cnt += 1

print(cnt)
