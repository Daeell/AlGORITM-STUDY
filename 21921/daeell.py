import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def solution():
    n, x = map(int, input().split())
    visitor = list(map(int, input().split()))

    if sum(visitor) == 0:
        return "SAD"

    curr_sum = sum(visitor[:x])
    max_sum = curr_sum
    max_count = 1

    for i in range(x, n):
        curr_sum += visitor[i] - visitor[i - x]

        if curr_sum == max_sum:
            max_count += 1
        elif curr_sum > max_sum:
            max_sum = curr_sum
            max_count = 1

    if max_sum == 0:
        return "SAD"
    else:
        return f'{max_sum}\n{max_count}'


print(solution())
