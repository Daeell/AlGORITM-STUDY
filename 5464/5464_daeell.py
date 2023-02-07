import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
parking_lot = dict()
for i in range(n+1):
    parking_lot[i] = 0
waiting = deque()
unit_charge = []
weight = []
fee = 0
print(n, m)

for _ in range(n):
    unit_charge.append(int(input()))
print(unit_charge)
for _ in range(m):
    weight.append(int(input()))
print(weight)

while(1):
    try:
        case = int(input())
        if (case > 0):
            for i in range(n+1):
                if(parking_lot[i] == 0):
                    parking_lot[i] == weight[case]
                else:
                    continue
        else:
            case = abs(case)
            parking_lot.index(weight[case])
            fee += weight[case]
    except:
        break
