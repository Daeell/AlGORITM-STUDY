def solution(cap, n, deliveries, pickups):
    answer = -1
    print(deliveries)
    print(pickups)
    
    tmpCap = cap #배달 할 때 각 시점에 트럭에 남은 자리 
    tmpPickCap = cap #픽업 할 때 각 시점에 트럭에 남은 자리 

    startDelivery = n-1
    startPickup = n-1
    
    for i in range(startDelivery, -1, -1) :
        # deliver
        if (deliveries[i]<=tmpCap) : 
            tmpCap -= deliveries[i]
            deliveries[i] = 0 
        else: #담을 수 있는 것보다 더 큰 경우 
            deliveries[i] -= tmpCap
            tmpCap = 0 
        if tmpCap == 0 : # 담을 수 있는 만큼 최대로 담았다면
            # 픽업 시작
            for j in range(startPickup, -1,-1):
                if ([pickups][j]<=tmpPickCap) :
                    tmpPickCap -= pickups[j]
                    pickups[i] = 0 
                else: 
                    #담을 수 있는 것보다 더 큰 경우 
                    pickups[i] -= tmpPickCap
                    tmpPickCap = 0 
                if tmpPickCap == 0 : 
                    #배달을 시작한 곳과 픽업을 시작한 곳 중 더 큰 값으로 거리 저장 
                    answer += (max(startDelivery, startPickup) +1)*2 # 거리 저장 
                    #startDelivery, startPickup 값 업데이트 
                    startDelivery = i # 현재 i까지 왔다는 걸 저장
                    startPickup = j 
                    break
            break
        
    return answer
