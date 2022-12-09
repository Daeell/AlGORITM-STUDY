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
        if number in nodes:
            idx = nodes.index(number)
            nodes[idx] = deleted
            deep_del(number)
            deep_del(idx)
        else:
            break


nodes[d_node] = deleted
deep_del(d_node)

for i in range(len(nodes)):
    if nodes[i] != deleted and i not in nodes:
        cnt += 1

print(cnt)
