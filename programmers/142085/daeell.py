def solution(n, k, enemy):
    # 매 라운드에서 막을 수 있는 최대 적의 수 계산
    max_enemies = []
    for e in enemy:
        max_enemies.append(min(n, n - e))
        n -= e

    # 최대한 적의 수가 많은 라운드에서 무적권 사용
    for i in range(len(max_enemies)):
        if k > 0 and max_enemies[i] > 0:
            k -= 1
            max_enemies[i] = 0

    # 모든 라운드를 막을 수 있는지 확인
    for e in max_enemies:
        if e > n:
            return max_enemies.index(e)
    return len(max_enemies)


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))

# 틀림
# def solution(n, k, enemy):
#     answer = 0
#     soldiers = n
#     for e in enemy:
#         if soldiers < e:
#             if k > 0:
#                 k -= 1
#             else:
#                 break
#         soldiers -= e
#         answer += 1
#     return answer
