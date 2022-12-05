# 30840	72
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]
dp[0] = 1
# 최장 증가 수열의 길이를 구한다. = 움직이지 않아도 되는 사람들의 수
maxV = 0
for i in range(1, n):
    # i가 가장 마지막에 위치한 수열.
    for j in range(0, i):
        if numbers[j] < numbers[i]:
            # 증가하는 수열이라면,
            maxV = max(maxV, dp[j])
            # 증가 수열의 길이의 최대 길이를 갱신한다.
    dp[i] = maxV+1
    # dp에 최장 증가 수열의 길이를 저장한다.
    maxV = 0
    # 다시 0으로 초기화하는 이유, 수열 길이의 최댓값을 갱신해주기 위해서 가능한 최솟값으로 갱신

print(n - max(dp))
# 움직여야할 최소 사람의 숫자는 (총 인원 - 움직이지 않아도 되는 사람들의 수)


# 스왑으로 해결하려 했는데 실패...
# tmp = 0
# cnt = 0
# # (1~n까지) 모든 숫자들이 다 있음. -> 해당 인덱스에 해당 숫자가 있으면 됨.
# for i in range(n):
#     numbers.append(int(input()))

# # 중요한 것은 모든 숫자들이 다 자신의 자리에 있어야 된다는 것을 의미한다.
# for i in range(1, len(numbers)):
#     # 만약에 해당하는 숫자가 그 위치에 없으면 그 위치에 있는 숫자와 스왑한다.
#     if i != numbers[i]:
#         idx = numbers.index(i)  # i가 있던 곳을 저장한다.
#         tmp = numbers[i]  # i의 고향에 있던 숫자를 저장한다.
#         numbers[i] = i  # i는 i의 고향으로 돌아간다.
#         numbers[idx] = tmp  # i가 살던 곳에는 다른 스왑하는 숫자가 들어간다.
#         cnt += 1
#     else:
#         continue
# print(cnt)
# print(numbers)
