import heapq
from collections import defaultdict


def solution(genres, plays):
    answer = []
    genre_total_play = defaultdict(int)
    genre_align = defaultdict(list)
    temp = list(zip(genres, plays))
    
    for i in range(len(genres)):
        genre_total_play[temp[i][0]] +=temp[i][1]
        heapq.heappush(genre_align[temp[i][0]], (-temp[i][1], i))
    
    sorted_genre = sorted(genre_total_play.items(), key=lambda x: -x[1])
    for ge, _ in sorted_genre:
        cnt =0
        while genre_align[ge]:
            _,num = heapq.heappop(genre_align[ge])
            answer.append(num)
            cnt +=1
            if cnt ==2:
                break
            

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))