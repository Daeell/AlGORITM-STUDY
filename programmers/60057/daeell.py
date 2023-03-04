def solution(s):
    if len(s) == 1:
        return 1

    answer = len(s)
    for unit in range(1, len(s)//2+1):
        prev = s[:unit]
        count = 1
        compressed = ""

        for i in range(unit, len(s), unit):
            curr = s[i:i+unit]
            if curr == prev:
                count += 1
            else:
                if count > 1:
                    compressed += str(count)
                compressed += prev
                prev = curr
                count = 1

        if count > 1:
            compressed += str(count)
        compressed += prev
        answer = min(answer, len(compressed))

    return answer
