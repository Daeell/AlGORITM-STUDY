import sys
sys.stdin = open("input.txt","r")

K = int(input())
nums = input()
answer = 0 
for i in nums :
    answer += int(i)

print(answer)
