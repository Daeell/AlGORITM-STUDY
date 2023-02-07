def solution(n, info):
    global answer, max_gap, visited
    answer = [0]*11
    max_gap = 0
    visited = set()

    WEIGHT = [10,9,8,7,6,5,4,3,2,1,0]

    def DFS(n, scoreboard):
        global answer, max_gap, visited
        if n == 0:
            ryan, apeach = 0, 0
            for i in range(11):
                if info[i] < scoreboard[i] and scoreboard[i] > 0:
                    ryan += WEIGHT[i]
                elif info[i] > 0:
                    apeach += WEIGHT[i]
            if ryan > apeach and ryan-apeach >= max_gap:
                if ryan-apeach == max_gap:
                    for i in range(10, -1, -1):
                        if answer[i] != scoreboard[i]:
                            if answer[i] < scoreboard[i]:
                                for j in range(11):
                                    answer[j] = scoreboard[j]
                                max_gap = ryan-apeach
                            break
                else:
                    for j in range(11):
                        answer[j] = scoreboard[j]
                    max_gap = ryan-apeach
            return

        for i in range(11):
            scoreboard[i] += 1
            if tuple(scoreboard) not in visited:
                visited.add(tuple(scoreboard))
                DFS(n-1, scoreboard)
            scoreboard[i] -= 1
    
    DFS(n, [0]*11)

    return answer if answer != [0]*11 else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))