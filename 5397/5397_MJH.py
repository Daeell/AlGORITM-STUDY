TESTCASE = int(input())

def main():
    inputString = input()
    answerString = []
    p = 0 # pointer
    for i in range(len(inputString)):
        if inputString[i] == '<':
            if p > 0:
                p -= 1

        elif inputString[i] == '>':
            if p < len(answerString):
                p += 1

        elif inputString[i] == '-':
            if p > 0:
                p -= 1
                answerString.pop(p)

        else:
            answerString.insert(p, inputString[i])
            p += 1
    
    answer = "".join(answerString)
    print(answer)

for _ in range(TESTCASE):
    main()