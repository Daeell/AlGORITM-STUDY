import sys

N = int(sys.stdin.readline())
schedule =[]
for _ in range(N):
    S = schedule.append(tuple(map(int, sys.stdin.readline().split())))

schedule_s = sorted(schedule, key = lambda x:(x[0],x[1]))
# schedule_e = sorted(schedule, key = lambda x:x[1])

print(schedule_s)
# print(schedule_e)
max_number = 1000000001
cnt = N
hard_to_solve = []
for i in range(N):
    end = schedule_s[i][1]
    for j in range(i+1,N):
        if end == schedule_s[j][0] or end < schedule_s[j][0]:
            # hard_to_solve.append(i)
            if schedule_s[i] and schedule_s[j] not in hard_to_solve:
                hard_to_solve.extend([schedule_s[i],schedule_s[j]])

        else:
            if schedule_s[i] not in hard_to_solve:
                hard_to_solve.append(schedule_s[i])
    
    # ans = min(cnt, max_number)        
print(set(hard_to_solve))
print(len(set(hard_to_solve)))
# print(ans)
