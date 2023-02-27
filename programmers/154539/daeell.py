def solution(numbers):
    length = len(numbers)
    answer = [-1]*length
    stk = []

    for i in range(length):
        while stk and numbers[stk[-1]] < numbers[i]:
            idx = stk.pop()
            answer[idx] = numbers[i]
        stk.append(i)
    return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
