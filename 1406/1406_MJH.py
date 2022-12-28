import sys
input = sys.stdin.readline

def command(strL:list, strR:list, args:str):
    if args == 'L':
        if len(strL) > 0:
            strR.append(strL.pop())

    elif args == 'D':
        if len(strR) > 0:
            strL.append(strR.pop())

    elif args == 'B':
        if len(strL) > 0:
            strL.pop()

    else:
        strL.append(args[2])

    return strL, strR


def main() -> None:
    strL = list(input().strip())
    strR = []
    for _ in range(int(input().strip())):
        strL, strR = command(strL, strR, input().strip())
    strR.reverse()
    print(''.join(strL + strR))


main()