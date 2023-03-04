# ALL PASSED
def solution(people, limit):
    answer = 0

    people.sort()
    j = 0
    for i in range(len(people)-1, -1, -1):
        if people[i] > limit-40:
            answer += 1
            continue
        if j > i:
            break
        if people[j] + people[i] <= limit:
            j += 1
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))