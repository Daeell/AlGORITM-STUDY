from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque([(begin, 0)])
    v = set()

    while q:
        w, l = q.popleft()
        if w == target:
            return l
        for nw in words:
            if trans_check(w, nw) and nw not in v:
                v.add(nw)
                q.append((nw, l+1))

    return answer


def trans_check(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
        if count > 1:
            return False
    return count == 1


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
