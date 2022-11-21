import sys
from itertools import product
input = sys.stdin.readline

def go():
    wNumber = int(input())
    wList = []
    wIndex = {}
    index = 0
    for _ in range(wNumber):
        wName, wCategory = input().split()
        if wCategory not in wIndex:
            wIndex[wCategory] = index
            wList.append(['NULL'])
            index += 1

        wList[wIndex[wCategory]].append(wName)
    
    print(len(list(product(*wList)))-1)




TESTCASE = int(input())

for _ in range(TESTCASE):
    go()