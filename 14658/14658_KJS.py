import sys
import heapq
width,cerro,tram,star = map(int, sys.stdin.readline().split())
star_coordinate = [[0] * (width+1) for _ in range(cerro+1)]
def countingstar(k,y,tram):
    max_num = 0
    count = 0
    for i in range(y,y+tram+1):
        for j in range(k,k+tram+1):
            if star_coordinate[i][j] == 1:
                count +=1
    count = max(max_num,count)
    return count
real_count = 0
que = []
for _ in range(star):
    a, b = map(int,sys.stdin.readline().split())
    star_coordinate[b][a] = 1
    heapq.heappush(que,(b,a))
for _ in range(star):
    c, d = heapq.heappop(que)
    real_count - max(real_count,countingstar(d,c,tram))


print(star-real_count)
# for y in range(1,cerro-tram+1):
#     for k in range(1,width-tram+1):
#         # countingstar(k,y,tram)
#         real_count = max(real_count,countingstar(k,y,tram))
        
        # for i in range(k,tram+1):
        #     for j in range(y,tram+1):
        #         if star_coordinate[i][j] == 1:
        #             count +=1
        #             count = max(max_num,count)
        #             print(count)
# for i in range(tram):
#     for j in range(tram):
#         if star_coordinate[i][j] == 1:
#             count +=1
# count = max(max_num,count)
    # print(count)

# print(count)
