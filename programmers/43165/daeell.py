def solution(numbers, target):
    answer = 0
    answer += dfs(0, 0, target, numbers)
    return answer


def dfs(curr_sum, idx, target, numbers):
    if idx == len(numbers):
        if curr_sum == target:
            return 1
        else:
            return 0
    else:
        cnt = 0
        cnt += dfs(curr_sum + numbers[idx], idx+1, target, numbers)
        cnt += dfs(curr_sum - numbers[idx], idx+1, target, numbers)
        return cnt


print(solution([1, 1, 1, 1, 1], 3))
