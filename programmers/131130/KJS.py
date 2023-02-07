def solution(cards):
    answer = []
    
    for i in range(len(cards)):
        group = []
        while cards[i] not in group:
            group.append(cards[i])
            i = cards[i] - 1
        if sorted(group) not in answer:
            answer.append(sorted(group))
        else:
            answer.append([])
    answer.sort(key = lambda x: len(x))
        
    return len(answer[-1]) * len(answer[-2])
