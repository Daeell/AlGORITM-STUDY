def solution(cap, n, deliveries, pickups):
    answer = 0
    def deliver():
        while True:
            if cur_cap - deliveries[cur_deli] >= 0:
                cur_cap -= deliveries[cur_deli]
                cur_deli -= 1
            else:
                deliveries[cur_deli] - cur_cap
                break
    def pickup():
        while True:
            if cur_cap - pickups[cur_pick] >= 0:
                cur_cap -= pickups[cur_pick]
                cur_pick -= 1
            else:
                pickups[cur_pick] - cur_cap
                break
    while cur_deli > 0 or cur_pick > 0:
        if cur_deli > 0:
            deliver()
        if cur_pick > 0:
            pickup()
    cur_cap = cap
    cur_deli = n-1
    cur_pick = n-1
    
    return answer