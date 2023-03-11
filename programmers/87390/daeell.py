def solution(n, left, right):
    arr = []
    for i in range(left, right+1):
        row = i // n
        col = i % n
        val = max(row, col) + 1
        arr.append(val)
    return arr


print(solution(3, 2, 5))
