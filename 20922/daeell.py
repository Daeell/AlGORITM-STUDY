def solution():
    # 수열에서 같은 원소가 K개 이하로 들어있는 수열의 최대 길이를 구한다.
    # 정수는 100,000이하, 수열의 길이는 n, 정수 개수 제한은 k
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    st, end = 0, 0
    cnt = [0] * 100001
    res = 0

    while st < n:
        if cnt[nums[st]] != k:
            cnt[nums[st]] += 1
            st += 1
        else:
            cnt[nums[end]] -= 1
            end += 1

        res = max(res, st - end)

    return res


print(solution())
