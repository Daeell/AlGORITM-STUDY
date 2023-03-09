from heapq import *

def solution(book_time):

    if len(book_time) == 1 :
        return 1
    
    tmp = []
    for book_list in book_time :
        start = book_list[0][:2] + book_list[0][3:5]
        end = book_list[1][:2] + book_list[1][3:5]
        tmp.append([int(start),int(end)])
    tmp = sorted(tmp, key = lambda x : (x[0], x[1]))
    
    playing_list = []
    for room in tmp :
        if not playing_list :
            heappush(playing_list, room[1])
        else :
            if int(str(min(playing_list))[-2:]) >= 50 :
                if room[0] < min(playing_list)+50 :
                    heappush(playing_list, room[1])
                else :
                    heappop(playing_list)
                    heappush(playing_list, room[1])
            else :
                if room[0] < min(playing_list)+10 :
                    heappush(playing_list, room[1])
                else :
                    heappop(playing_list)
                    heappush(playing_list, room[1])
    answer= len(playing_list)
        
    return answer
