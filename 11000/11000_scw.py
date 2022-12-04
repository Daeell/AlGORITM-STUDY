#강의실 배정
import sys, heapq
input=sys.stdin.readline

N = int(input().strip())

A=[]
for _ in range(N):
    A.append(list(map(int,input().strip().split())))

A.sort(key=lambda x:(x[0], x[1]))

room = []
heapq.heappush(room, A[0][1])

for i in range(1, N):
    if A[i][0]<room[0]:
        heapq.heappush(room,A[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,A[i][1])

print(len(room))


# while(A):
#     s, e = A.popleft()
#     if len(room) == 0 :
#         room[room_num].append(s)
#         room[room_num].append(e)
#         room_num +=1
#     else:
#         for i in range(len(room)):
#             room_s, room_e = room[i]
#             if room_e <= s :
#                 room[i][0]=s
#                 room[i][1]=e
#                 room_num +=1
#                 break
#             elif i == room_num-1:
#                 room[room_num].append(s)
#                 room[room_num].append(e)
#                 room_num +=1

# print(room_num-1)
                    
