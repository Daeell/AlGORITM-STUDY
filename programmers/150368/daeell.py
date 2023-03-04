from itertools import product


def solution(users, emoticons):
    answer = [-1, -1]

    # 가능한 이모티콘 할인율 조합을 모두 생성합니다.
    discount_rates = range(10, 41, 10)
    for discounts in product(discount_rates, repeat=len(emoticons)):
        cost = 0  # 총 구매 비용을 저장할 변수
        new_users = 0  # 새로운 이모티콘 구매자 수를 저장할 변수

        for user in users:
            # 해당 사용자의 총 구매 비용을 계산합니다.
            user_cost = 0
            for i, rate in enumerate(discounts):
                if rate >= user[0]:  # 할인율이 구매 기준 이상인 경우
                    user_cost += emoticons[i] * \
                        (100 - rate) // 100  # 할인된 가격 계산
            if user_cost >= user[1]:  # 총 구매 비용이 사용자의 구매 기준 이상인 경우
                new_users += 1
            cost += user_cost

        if new_users > answer[0]:  # 새로운 이모티콘 구매자 수가 더 많은 경우
            answer = [new_users, cost]
        elif new_users == answer[0]:  # 새로운 이모티콘 구매자 수가 같은 경우
            answer[1] = max(answer[1], cost)  # 총 구매 비용이 더 큰 값으로 업데이트합니다.

    return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
