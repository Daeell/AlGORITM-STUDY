first = list(input())
bomb = list(input())

# print(first, bomb)

word = []
num = len(bomb)
for tmp in first :
    word.append(tmp)
    while word[-1*(num):] == bomb :
        for _ in range(num) :
            word.pop()

if word :
    print("".join(word))
else :
    print("FRULA")
