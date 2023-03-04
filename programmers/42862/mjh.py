# PASSED
def solution(n, lost, reserve):
    answer = 0

    arr = [1]*n

    for e in lost:
        arr[e-1] -= 1
    for e in reserve:
        arr[e-1] += 1
    
    for i in range(len(arr)):
        if arr[i] >= 1:
            answer += 1
            continue
        if i != 0 and arr[i-1] >= 2:
            answer += 1
            continue
        if i != len(arr)-1 and arr[i+1] >= 2:
            arr[i+1] -= 1
            answer += 1

    return answer

print(solution(5, [2, 4], [1, 3, 5]))