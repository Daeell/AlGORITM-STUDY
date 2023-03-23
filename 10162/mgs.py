timer = int(input())
time_list = [300, 60, 10]
dp = [0] * 10001

if timer % 10 != 0 :
    print(-1)
    exit()

ans = []
for time in time_list :
    tmp = timer//time
    timer %= time
    ans.append(str(tmp))

print(" ".join(ans))
