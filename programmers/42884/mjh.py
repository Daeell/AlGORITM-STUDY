# 못 품
def solution(routes):
    answer = 1

    # 진입 시점이 진출 시점보다 큰 입력값이 있나?
    for i in range(len(routes)):
        if routes[i][0] > routes[i][1]:
            tmp = routes[i][0]
            routes[i][0] = routes[i][1]
            routes[i][1] = tmp

    routes.sort(key=lambda x: (x[0], -x[1]))
    last_exit_point = routes[0][1]
    current_longest_point = routes[0][1]

    for i in range(len(routes)):
        enter, exit = routes[i]
        if exit > current_longest_point:
            current_longest_point = exit
        if enter > last_exit_point:
            answer += 1
            last_exit_point = current_longest_point

    return answer