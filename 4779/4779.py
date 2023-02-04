import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

list_ = []
while(1):
    try:
        list_.append(int(input()))
    except:
        break


def line(x, word):
    string = []
    num = 3**x
    if x == 0:
        string.append('-')
        return string
    if x == 1:
        for i in range(1, num+1):
            if i % 2 == 1:
                string.append(word)
            else:
                string.append('')
        return string
    else:
        if x % 2 == 0:
            line(1, '-')+line(x-1, '-')
        else:
            line(1, ' ')+line(x-1, ' ')


for i in list_:
    if i % 2 == 0:
        print(line(i, ''))
    else:
        print(line(i, '-'))
