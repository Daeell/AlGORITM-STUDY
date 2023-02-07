def solution(k, dungeons):
    global answer
    answer = 0

    visited = set()
    def recur(visited, left, cnt):
        global answer
        for i in range(len(dungeons)):
            if i not in visited and left >= dungeons[i][0] and left - dungeons[i][1] >= 0:
                visited.add(i)
                recur(visited, left-dungeons[i][1], cnt+1)
                visited.remove(i)
        if cnt > answer:
            answer = cnt
            return

    recur(visited, k, 0)

    return answer

# print(solution(80, [[80,20],[50,40],[30,10]]))