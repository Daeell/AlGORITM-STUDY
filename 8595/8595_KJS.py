import sys
X = int(sys.stdin.readline())
good = list(sys.stdin.readline().strip())

num = []
cnt = 0
idx = 0
fix = []
for i in range(len(good)):
    if 48<= ord(good[i]) <=57:
        num.append(good[i])
        # print(num)
        cnt += 1
        # print(cnt)
    else:
        cnt +=1
        # print(cnt)
        if cnt > len(num):
            print(idx)
            hap="".join(num[idx:])
            fix.append(hap)
            num[idx] = hap
            idx += 1
            cnt = len(num)
        print(num)
