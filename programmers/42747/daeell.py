def solution(citations):
    citations = sorted(citations, reverse=True)
    h_index = 0
    for i in range(len(citations)):
        if citations[i] >= i+1:
            h_index = i+1
        else:
            break
    return h_index
