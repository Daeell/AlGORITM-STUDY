#히든 넘버
import sys, re
input=sys.stdin.readline

N= int(input().strip())

string=input().strip()

numbers = re.findall(r'\d+', string)
print(sum(map(int,numbers)))