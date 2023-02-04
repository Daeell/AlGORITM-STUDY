def solution(cards):
    answer = 0

    for i in range(len(cards)):
        first_picked = set()
        first_picked.add(i)
        iterator = i
        while len(first_picked) < len(cards):
            if cards[iterator]-1 in first_picked:
                break
            first_picked.add(cards[iterator]-1)
            iterator = cards[iterator]-1

        for j in range(len(cards)):
            second_picked = set()
            if j not in first_picked:
                second_picked.add(j)
                iterator = j
                while len(first_picked)+len(second_picked) < len(cards):
                    if cards[iterator]-1 in first_picked or cards[iterator]-1 in second_picked:
                        break
                    second_picked.add(cards[iterator]-1)
                    iterator = cards[iterator]-1

                answer = max(answer, len(first_picked)*len(second_picked))

    return answer

print(solution([8,6,3,7,2,5,1,4]))