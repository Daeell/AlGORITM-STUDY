def solution(cap, n, deliveries, pickups):
    answer = -1
    deliveries.reverse()
    pickups.reverse()
    
    
    del_sum = 0
    pic_sum = 0
    
    for i in range(n):
        if del_sum + deliveries[i] < cap and pic_sum + pickups[i] < cap:
                del_sum += deliveries[i]
                pic_sum += pickups[i]
            else:
    
    
    
    # d_sum = 0
    # max_length = n
    # distance = []
    # deliveries.reverse()
    # for i in range(0,n):
    #     if deliveries[i] != 0 and d_sum == 0:
    #         distance.append(n-i)
    #     d_sum += deliveries[i]
    #     if d_sum // cap >= 1 and d_sum % cap !=0:
    #         distance.append(n-i)
    #         d_sum = d_sum % cap
    # print(distance)
    
    
#     # 테스트케이스만 통과 
#     merge = []
#     for i in range(n):
#         a = deliveries[i]
#         b = -pickups[i]
#         merge.append(a+b)
    
#     print(merge)
#     res = 0
#     for i in range(n):
#         if i ==0:
#             continue
#         if merge[i] > 0:
#            res += i+1
#     answer = 2*res
    

            
    # 가장 많이 들고 가서 가장 많이 가져와야한다....
    return answer

