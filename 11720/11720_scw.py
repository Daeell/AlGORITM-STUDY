#숫자의 합
import sys
input=sys.stdin.readline

N= int(input().strip())

print(sum(map(int,(list(input().strip())))))