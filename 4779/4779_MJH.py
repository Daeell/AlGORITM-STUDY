import sys

def recursion(depth):
    if depth == 0:
        print('-', end='')
    else:
        recursion(depth-1)
        n = 3**(depth-1)
        for i in range(n):
            print(' ', end='')
        recursion(depth-1)

testcase = sys.stdin.readlines()
for case in testcase:
    recursion(int(case))
    print()