from itertools import permutations


def solution(k, dungeons):
    dungeonsRoute = list(permutations(dungeons))
    answer = -1
    visited = 0
    piro = k
    for route in dungeonsRoute:
        for dungeon in route:
            if piro >= dungeon[0]:
                piro -= dungeon[1]
                visited += 1
        answer = max(answer, visited)
        visited = 0
        piro = k
    return answer
