import heapq
def solution(n, works):
    answer = 0
#     works.sort(reverse=True)
     
#     while n >0 and sum(works) > 0:
#         for i in range(len(works)):
#             if works[i] == 0:
#                 continue
#             if i == len(works)-1:
#                 if works[i] > works[i-1]:
#                     works[i] -=1
#                     n -=1
#             else:
#                 if works[i] > works[i+1]:
#                     works[i] -= 1
#                     n -= 1
#                     if works[i] == works[i+1]:
#                         break
#                 elif works[i] == works[i+1]:
#                     works[i] -= 1
#                     n -= 1
#             print(n,works[i])
#             if n == 0 or sum(works) == 0:
#                 break
    heapq.heapify(works)
    print(works)
    
    
    
    
    for i in range(len(works)):
        if works[i] <=0:
            continue
        else:
            answer += (works[i])**2
            
    return answer
