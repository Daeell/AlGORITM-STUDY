def solution(numbers):
    answer = []
    for x in numbers:
        # 다음으로 큰 숫자를 찾습니다.
        next_num = find_next_num(x)
        answer.append(next_num)
    return answer


def find_next_num(x):
    # x의 비트 개수를 세어줍니다.
    count = bin(x).count('1')

    # 다음으로 큰 숫자를 찾습니다.
    while True:
        x += 1
        # x의 비트 개수를 세어줍니다.
        cnt = bin(x).count('1')

        # x와 다른 비트 개수가 1~2인 수를 찾습니다.
        if cnt == count or cnt == count+1 or cnt == count+2:
            return x


print(solution([2, 7]))
