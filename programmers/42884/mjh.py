# 정답입니다!
def solution(routes):
    answer = 1
    routes.sort()
    last_exit_point = routes[0][1]
    for i in range(len(routes)):
        enter, exit = routes[i]
        if enter > last_exit_point:
            answer += 1
            last_exit_point = exit
        else:
            if exit < last_exit_point:
                last_exit_point = exit
    return answer