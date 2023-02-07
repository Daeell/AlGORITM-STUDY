import sys
from bisect import bisect_left
input = sys.stdin.readline


def main():
    n = int(input())
    nlist = list(map(int, input().split()))
    lis = []
    for i in range(n):
        if i == 0:
            lis.append(nlist[i])

        elif lis[-1] < nlist[i]:
            lis.append(nlist[i])

        else:
            idx = bisect_left(lis, nlist[i])
            lis[idx] = nlist[i]

    print(len(lis))


main()
