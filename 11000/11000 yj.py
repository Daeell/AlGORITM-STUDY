import sys
sys.stdin = open("input.txt", "r")
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
lecture = []
for i in range (N) :
    lecture.append(tuple(map(int, input().split())))

lecture.sort(key=lambda x : -x[1])

room = defaultdict(list)
flag = False
for i in range (N) : 
    l = lecture[i]
    if ( not room ) : # 아직 아무 회의실도 없다면 
        room[0].append(l[0]) # 0번 회의실로 현재 강의의 시작하는 시간 추가 
    else :
         # 회의실이 존재하는 상태
         # 강의 종료 시간 이상의 시작 시간을 가진 회의실 중 가장 그 갭이 작은 회의실 배정 
         # 내 끝나는 시간 이상의 시작 시간인 회의실이 없다면 새 회의실 배정 
         # ? 최소 힙을 사용해서 시간을 줄일 수 있는 방법은 없을까? 
         min_gap = [sys.maxsize, 0] # gap, 해당 회의실 

         k = len(room)
         for i in range(k) :  # 회의실 순회 
            gap = room[i][-1] - l[1] # 해당 회의실의 시작 시간 - 강의의 종료 시간
            if gap >= 0 : 
                if min_gap[0] > gap : # 더 작은 값  
                    min_gap[0] = gap 
                    min_gap[1] = i 
                    flag = True # 어쨋든 기존 회의실을 쓸 수 있다는 얘기 
            if (flag) : 
                room[min_gap[1]].append(l[0])
            else:    
                room[k].append(l[0])
print(len(room))
