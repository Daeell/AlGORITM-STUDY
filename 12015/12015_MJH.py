from bisect import bisect_left
def main():
    N = int(input())
    inputs = list(map(int, input().split()))

    arr = []
    arr.append(inputs[0])

    for i in range(1, N):
        n = inputs[i]
        if arr[-1] < n:
            arr.append(n)
        else:
            arr[bisect_left(arr, n)] = n

    print(len(arr))

main()