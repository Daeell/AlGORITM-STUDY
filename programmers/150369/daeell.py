def solution(cap, n, deliveries, pickups):
    deliver = 0
    res = 0
    answer = 0
    for i in range(n):
        if (deliveries[i] != 0 or pickups[i] != 0):
            cnt = 0
            while(deliver < deliveries[i] or res < pickups[i]):
                cnt += 1
                deliver += cap
                res += cap
            deliver -= deliveries[i]
            res -= pickups[i]
        answer = answer + (i*cnt*2)

    return answer
