def solution(citations):
    answer = 0
    citations.sort()
    c = len(citations)
    for i in range(c):
        if citations[i] >= c-i:
            return c-i
    return answer

