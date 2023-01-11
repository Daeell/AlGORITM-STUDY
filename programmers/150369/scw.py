#택배 배달과 수거하기

def solution(cap, n, deliveries, pickups):
    length =0
    temp_length=0
    k=n
    d_z=deliveries.count(0)
    p_z=pickups.count(0)

    while True:
        for i in range(k-1,-1,-1):
            if(deliveries[i] !=0 or pickups[i] !=0):
                temp_length=i
                break

        k = temp_length
        length += (temp_length+1)*2        
        
        if d_z != n or p_z !=n:
            d_z_temp = 0
            p_z_temp = 0
            for i in range(temp_length, -1, -1):
                if p_z_temp == cap and d_z_temp == cap:
                    break
                if d_z_temp < cap and d_z_temp + deliveries[i]<=cap and deliveries[i] !=0:
                    d_z_temp += deliveries[i]
                    deliveries[i] = 0
                    d_z+=1
                if p_z_temp < cap and p_z_temp + pickups[i]<=cap and pickups[i] !=0:
                    p_z_temp += pickups[i]
                    pickups[i] = 0
                    p_z+=1
                    

        if d_z == n and p_z == n:
            break

    answer = length
    
    return answer