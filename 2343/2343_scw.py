# #기타 레슨
# import sys
# input=sys.stdin.readline

# n, m = map(int, input().strip().split())

# A=list(map(int, input().strip().split()))


# if n == m :
#     print(max(A))
#     exit(0)

# else:
#     s = max(A) # 이분 탐색 시작점
#     e = sum(A) # 이분 탐색 끝점
#     real_answer=1000000001
#     while s <= e :
#         mid = (s+e)//2
        
#         cnt = 1 # bluelay 의 개수    
#         answer_temp =0 # bluelay 1개의 값    

#         for i in A:
#             if cnt > m: # cnt가 m을 넘으면 더 탐색할 필요가 없음
#                 break
            
#             if answer_temp + i <= mid: # mid까지 answer_temp의 합을 구함
#                 answer_temp +=i
#             else: # 그게 아니면 cnt를 1개 올리고 탐색을 실행
#                 cnt +=1
#                 answer_temp = i

#         if cnt > m: # 만약 cnt가 m보다 많으면 --> mid가 너무 작다 라는 의미
#             s = mid +1 # mid가 너무 작기 때문에 s를 mid로 올려줌
#         else : # cnt가 m보다 작거나 같으면 
#             e = mid -1 # end를 mid로 내려주고
#             if mid >= max(A): # 이떄의 mid가 max(A) 보다 크다면 --> max(A)보다는 더 작아질수 없음
#                 real_answer=min(real_answer, mid) # 최소값을 넣어준다
#     print(real_answer)


#기타 레슨
import sys
input=sys.stdin.readline

n, m = map(int, input().strip().split())

A=list(map(int, input().strip().split()))


if n == m :
    print(max(A))
    exit(0)
else:
    s = max(A) # 이분 탐색 시작점
    e = sum(A) # 이분 탐색 끝점
    real_answer=1000000001
    while s <= e :
        mid = (s+e)//2
        
        cnt = 1 # bluelay 의 개수    
        answer_temp =0 # bluelay 1개의 값    

        for i in A:
            if cnt > m: # cnt가 m을 넘으면 더 탐색할 필요가 없음
                break
            
            if answer_temp + i <= mid: # mid까지 answer_temp의 합을 구함
                answer_temp +=i
            else: # 그게 아니면 cnt를 1개 올리고 탐색을 실행
                cnt +=1
                answer_temp = i

        if cnt > m: # 만약 cnt가 m보다 많으면 --> mid가 너무 작다 라는 의미
            s = mid +1 # mid가 너무 작기 때문에 s를 mid로 올려줌
        else : # cnt가 m보다 작거나 같으면 
            e = mid -1 # end를 mid로 내려주고
            if mid >= max(A): # 이떄의 mid가 max(A) 보다 크다면 --> max(A)보다는 더 작아질수 없음
                real_answer=min(real_answer, mid) # 최소값을 넣어준다
    print(real_answer)
