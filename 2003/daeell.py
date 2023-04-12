import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def solution():
    n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    count = 0
    start, end = 0, 0
    curr_sum = 0

    while end <= n:
        if curr_sum == m:
            count += 1
            curr_sum -= nums[start]
            start += 1

        elif curr_sum < m:
            if end == n:
                break
            curr_sum += nums[end]
            end += 1
        else:
            curr_sum -= nums[start]
            start += 1

    return count


print(solution())
