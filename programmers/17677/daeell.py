def solution(str1, str2):
    multi_set1, multi_set2 = [], []

    for i in range(len(str1)-1):
        token = str1[i:i+2].lower()
        if token.isalpha():
            multi_set1.append(token)
    for i in range(len(str2)-1):
        token = str2[i:i+2].lower()
        if token.isalpha():
            multi_set2.append(token)

    intersection = []
    for token in multi_set1:
        if token in multi_set2:
            intersection.append(token)
            multi_set2.remove(token)

    union = multi_set1 + multi_set2

    if len(union) == 0:
        return 65536
    else:
        return int(len(intersection) / len(union) * 65536)


print(solution("FRANCE", "french"))
