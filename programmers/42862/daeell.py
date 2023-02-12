def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)

    available = [1 for _ in range(n+1)]
    for i in lost:
        available[i] = 0
    for i in reserve:
        available[i] += 1

    for i in lost:
        if available[i] == 0:
            if available[i-1] == 2:
                available[i-1] = 1
                available[i] = 1
            elif available[i+1] == 2:
                available[i+1] = 1
                available[i] = 1

    return n - available.count(0)


print(solution(5, [2, 4], [1, 3, 5]))
