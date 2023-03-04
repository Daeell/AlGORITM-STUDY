def solution(n, m, section):
    answer = 0
    idx = 0
    max_ = section[idx] + m
    while idx < len(section):
        while idx < len(section) and section[idx] < max_:
            print(max_)
            idx += 1
        if idx == len(section):
            answer += 1
            break
        max_ = section[idx] + m
        answer += 1
    return answer


# print(solution(8, 4, [2, 3, 6]))

print(solution(4, 1, [1, 2, 3, 4]))
