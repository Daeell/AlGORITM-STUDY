def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]
    stack = [0]
    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i-idx
        stack.append(i)
    return answer


print(solution([1, 2, 3, 2, 3]))
