def solution(routes):
    routes.sort()
    answer = 1

    s,e = routes[0][0], routes[0][1]
    
    for i in range(1, len(routes)):
        if routes[i][0] <= e:
            s = routes[i][0]
            if routes[i][1] <e:
                e = routes[i][1]
        else:
            answer +=1
            s = routes[i][0]
            e = routes[i][1]
    
    return answer


print(solution([[-20,-15], [-19,-18],[-14,-5], [-18,-13], [-5,-3]]))