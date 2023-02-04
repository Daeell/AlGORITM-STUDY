def solution(k, tangerine):
    answer = 0
    counts = dict()
    for e in tangerine:
        if e not in counts:
            counts[e] = 1
        else:
            counts[e] += 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    i = 0
    while k > 0:
        k -= sorted_counts[i][1]
        answer += 1
        i += 1

    return answer

# print(solution(6, [1,3,2,5,4,5,2,3]))