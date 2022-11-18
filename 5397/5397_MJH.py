TESTCASE = int(input())

def main():
    inputString = input()
    leftStack = []
    rightStack = []

    for i in range(len(inputString)):
        if inputString[i] == '<':       # Case 1
            if len(leftStack) > 0:
                rightStack.append(leftStack.pop())

        elif inputString[i] == '>':     # Case 2
            if len(rightStack) > 0:
                leftStack.append(rightStack.pop())

        elif inputString[i] == '-':     # Case 3
            if len(leftStack) > 0:
                leftStack.pop()

        else:                           # Case 4
            leftStack.append(inputString[i])
    
    # begin print
    for i in range(len(leftStack)):
        print(leftStack[i], end='')
    for i in range(len(rightStack)-1, -1, -1):
        print(rightStack[i], end='')
    print()
    # end print

for _ in range(TESTCASE):
    main()