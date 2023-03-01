from collections import deque


def solution(progresses, speeds):
    answer = []
    q = deque()

    for p, s in zip(progresses, speeds):
        q.append((p, s))

    while q:
        cnt = 0
        while q and q[0][0] >= 100:
            q.popleft()
            cnt += 1

        if cnt > 0:
            answer.append(cnt)

        for i in range(len(q)):
            p, s = q[i]
            q[i] = (p+s, s)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
