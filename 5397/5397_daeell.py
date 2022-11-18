import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())

for _ in range(n):

    input_ = defaultdict(list)
    words = input()
    for i in range(len(words)):
        input_[i] = words[i]

    password = [[0]*(len(words)+1)]
    pointer = 1
    for i in range(len(input_)):
        if input_[i] == '<' and pointer > 0:
            pointer -= 1
            continue
        elif input_[i] == '>' and pointer <= len(password):
            pointer += 1
            continue
        elif input_[i] == '-':
            # password의 pointer 부분 삭제
            del(password[0][pointer])
            continue
        password[0][pointer] = input_[i]

    print(password)
