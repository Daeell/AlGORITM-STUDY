import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
time_table = [list(map(int, input().split())) for _ in range(n)]
time_table.sort(key=lambda x: (x[1], x[0]))
# 시간이 일찍 끝나는 강의순서대로 정렬한다. 같이 끝날 경우 일찍 시작하는 순서대로 배치한다.

rooms = []
heapq.heappush(rooms, time_table[0])

for i in range(1, n):
    earlytime = heapq.heappop(rooms)
    # 강의실을 최소로 쓰기 위해서는 힙을 사용해서 일찍 끝나는 강의실에서 최대한 많은 강의를 수행하도록 한다.
    if time_table[i][0] < earlytime[1]:
        # 강의가 시작하는 시간이 전의 강의 시간보다 빠른 경우
        heapq.heappush(rooms, earlytime)
        # 강의실을 늘린다.
    heapq.heappush(rooms, time_table[i])
    # 해당 강의를 추가한다.

print(len(rooms))


# 시간 초과...
# start = [(0, 0)]
# for time in time_table:
#     for i in range(len(start)):
#         if time[0] >= start[i][1]:
#             start[i] = time
#             break
#         elif(i == (len(start)-1)):
#             start.append(time)
#             break
