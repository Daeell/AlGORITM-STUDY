import sys
words = sys.stdin.readline().strip()
bombs = sys.stdin.readline().strip()
b = len(bombs)
answer = []
for word in words:
    answer.append(word)
    if ''.join(answer[-b:]) == bombs:
        for _ in range(b):
            answer.pop()
if answer:
    print(''.join(answer))
else:
    print('FRULA')
