def solution(n):
    nums = ['1', '2', '4']
    q, r = divmod(n - 1, 3)
    if q <= 0:
        return nums[r]
    else:
        return solution(q) + nums[r]


print(solution(123))
