import sys
sys.stdin = open('input.txt', 'r')
from collections import defaultdict 
from itertools import combinations
input = sys.stdin.readline

T = int(input())

def each_test () :
    N = int(input()) 
    items = defaultdict(int)
    for i in range(N):
        tmp = input().split()
        items[tmp[1].strip()] +=1 
    l = len(items)
    answer = 0 
    for i in range (1,l+1):
        combi = list(combinations(items, i))
        print(combi)
        for each in combi :
            tmp_answer = 1
            for j in range[i]: 
                tmp_answer *= items[j]





for i in range(T):
    each_test()