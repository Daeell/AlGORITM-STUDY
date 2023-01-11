def solution(cap, n, deliveries, pickups):
    answer = 0
    for i in range(n-1, -1, -1):
        if deliveries[i] != 0 or pickups[i] != 0:
            break
    p = i
    if i <= 0:
        return answer
    answer += (p+1)*2
    cap_deliver = 0
    cap_pickup = 0
    for i in range(p, -1, -1):
        cap_deliver += deliveries[i]
        cap_pickup += pickups[i]
        while cap_deliver > cap or cap_pickup > cap:
            answer += (i+1)*2
            cap_deliver -= cap
            cap_pickup -= cap

    return answer

# print(solution(10,2,[0,50],[50,0]))