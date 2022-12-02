import sys
input = sys.stdin.readline

def b_search(start, end, val, cmp_idx) -> int:
    answer = -1
    while start <= end:
        mid = (start + end) // 2
        if lecList[mid][cmp_idx] < val:
            start = mid+1
        else:
            if lecList[mid][2] == 0:
                answer = mid
            end = mid-1

    return answer
    

N = int(input())
lecList = []
for i in range(N):
    lecList.append(list(map(int, input().split()))+[0])

lecList.sort(key=lambda x: x[1])
lecList.sort(key=lambda x: x[0])

result = 0
for i in range(N):
    # If used, then continue
    if lecList[i][2] == 1:
        continue

    # Found unused lecture.
    result += 1
    lecList[i][2] = 1
    cur = i

    while cur+1 < N:
        idx = b_search(cur+1, N-1, lecList[cur][1], 0)
        if idx == -1:
            break
        else:
            lecList[idx][2] = 1
            cur = idx

print(result)