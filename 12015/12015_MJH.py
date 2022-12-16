def main():
    N = int(input())
    inputs = list(map(int, input().split()))

    arr = [0]*N

    for i in range(N-1, -1, -1):
        start = i
        end = N-1
        found = -1

        while start < end:
            mid = (start + end) // 2
            if arr[i] < arr[mid]:
                found = mid
                end = mid - 1
            else:
                start = mid - 1

        if found != -1:
            arr[i] = arr[mid] + 1
        else:
            arr[i] = 1

    print(max(arr))


main()