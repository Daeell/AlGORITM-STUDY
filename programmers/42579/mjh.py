# PASSED
from heapq import heappush, heappop
def solution(genres, plays):
    answer = []
    
    genres_counter = dict()
    
    for i in range(len(genres)):
        if genres[i] not in genres_counter:
            genres_counter[genres[i]] = []
        heappush(genres_counter[genres[i]], (-plays[i], i))
    
    genres_list = []
    for genre in genres_counter:
        count = 0
        for e in genres_counter[genre]:
            count += e[0]
        genres_list.append((count, genre))
    
    genres_list.sort()
    
    for count, genre in genres_list:
        append_cnt = 0
        while genres_counter[genre] and append_cnt < 2:
            answer.append(heappop(genres_counter[genre])[1])
            append_cnt += 1
    
    return answer